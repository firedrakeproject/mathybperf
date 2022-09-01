from .mesh import mesh_3D
from .form import mixed_poisson
from .space import RT_DQ_3D
from .solver import solve_with_params
from mathybperf.verification.error import check_error, check_var_problem, project_trace_solution
from mathybperf.verification.geometric import check_facetarea_and_cellvolume
from firedrake import *
import ufl
from math import ceil
from firedrake.petsc import PETSc


def problem(problem_bag, solver_bag, verification, new=True, project=False):
    reset = not problem_bag.mesh or new  # setup new problem
    if reset:
        problem_bag.mesh = mesh_3D(problem_bag, solver_bag.levels)
        solver_bag.mesh = problem_bag.mesh

    # calculate exact solution on the new mesh before we setup the forms because we do MMS
    exact_sol = solver_bag.exact_solution(problem_bag.scaling, problem_bag.exact_sol_type)

    if reset:
        problem_bag.space = RT_DQ_3D(problem_bag.order, problem_bag.mesh)
        problem_bag.var_problem, problem_bag.var_problem_repr, problem_bag.var_problem_info = mixed_poisson(problem_bag.space[0],
                                                                                                            problem_bag.add_to_quad_degree,
                                                                                                            exact_sol)

    # solve problem
    a, L, quadrature_degree = problem_bag.var_problem
    w, solver = solve_with_params(problem_bag, solver_bag)
    pc = solver.snes.ksp.pc.getPythonContext() if solver.snes.ksp.pc.getType() == "python" else None
    # compare iterative solution to reference solution
    if pc and hasattr(pc, "trace_solution"):
        w_t = pc.trace_solution
        problem_bag.total_local_shape = solver.snes.ksp.pc.getPythonContext().schur_builder.total_local_shape
    else:
        w_t = None
        problem_bag.total_local_shape = "NAN"
    w_t_exact = None
    w2 = None
    if project:
        if problem_bag.exact_sol_type == "quadratic":
            fc1 = {'quadrature_degree': 4+ceil((1+problem_bag.order+1+3)/2)}
            fc2 = {'quadrature_degree': 4+ceil((2+problem_bag.order+1)/2)}
        elif problem_bag.exact_sol_type == "exponential":
            d = 9+problem_bag.order
            fc1 = {'quadrature_degree': d+1}
            fc2 = {'quadrature_degree': d}
        else:
            d = 5+problem_bag.order
        # fc1 = {}
        # fc2 = {}
        w2 = Function(problem_bag.space[0])
        w2.sub(0).project(ufl.grad(exact_sol), solver_parameters={'ksp_rtol': 1.e-9, 'ksp_atol': 1.e-9}, form_compiler_parameters=fc1, use_slate_for_inverse=False)
        w2.sub(1).project(exact_sol, solver_parameters={'ksp_rtol': 1.e-9, 'ksp_atol': 1.e-9}, form_compiler_parameters=fc2, use_slate_for_inverse=False)
        if w_t:
            T = w_t.function_space()
            w_t_exact = Function(T).project(exact_sol,
                                            solver_parameters={'ksp_rtol': 1.e-9, 'ksp_atol': 1.e-9},
                                            form_compiler_parameters=fc2,
                                            use_slate_for_inverse=False)


    elif verification:
        parameters = {
            "ksp_type": "gmres",
            "ksp_gmres_restart": 100,
            "ksp_rtol": 1e-8,
            "pc_type": "ilu",
            }
        A = assemble(a)
        naivesolver = LinearSolver(A, solver_parameters=parameters)

        w2 = Function(problem_bag.space[0])
        b = assemble(L)
        naivesolver.solve(w2, b)

    # verification of error
    if verification:
        # check some geometric quantities
        if problem_bag.deformation == [0]:
            check_facetarea_and_cellvolume(problem_bag.space[2])

        # plug iterative solution in the variational problem
        check_var_problem(a, L, w, 1**(-problem_bag.order))

        # double check that the reference solution is solving the variational problem
        # (it always should, since we do MMS,
        # but choosing an exact solution that does not fulfill the BCs can screw things up
        # and choosing the quadrature degree too low, too.)
        check_var_problem(a, L, w2, 1**(-problem_bag.order))

        # compare iterative to reference solution
        check_error(w, w2, 10**(-problem_bag.order))

    return quadrature_degree, (w, w2), (w_t, w_t_exact), solver_bag.mesh, solver
