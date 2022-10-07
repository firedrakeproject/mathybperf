# Performance experiments for fully matrix-free high order hybridised compatible FEM

Poisson problems need to be solved in various physical setups. One of them is the Navier-Stokes equations: If the time derivative in the incompressible Navier-Stokes equations is solved with a predictor-evaluation-corrector scheme, a Poisson problem has to be solved at every time step for updating the pressure with the velocity prediction. The Poisson problem for the pressure can be rewritten into a mixed system by introduction of a flux variable. If the mixed spaces are chosen in a compatible way this has advantages, e.g. the conversation of some physical quantities. Mixed Poisson problems are difficult to solve because a) they have saddle-point structure and are indefinite and b) they are globally coupled and the condition number of the operator grows when refining its approximation. Hybridisation is used to remove most of the global coupling.

Hybridisation on high order FEM requires matrix-free infrastructure. The required code gen has been newly introduced in Firedrake and is tested for performance in this repo.

The mixed Poisson problem is solved with different solver setups, in most cases with a hybridisation preconditioner, but also with a PETSc fieldsplit preconditioner for a reference. Further, Gopalakrishnan-Tan multigrid (GTMG), which is expected to be a robust preconditioner for the trace system solve with respect to an increasing approximation degree, is investigated.

Different solver setups are compared, evaluating both runtime and the iteration count required for a converged solution. Further, the solvers are evaluated and compared with help of the Time-Size-Accuracy (TAS) spectrum. The spectrum is useful to compare different algorithms and discretisations considering accuracy and throughput rate on top of time-to-solution.

The data lies in `performance/results` and `performance/flames`. The results can be found in `performance/plots`.

All tests are verified in the actions. A validation should be added in the future.
