from firedrake import *

# Here are parameters defined used in the case files of my setups
# 1) HELPER DICTs

# MG params
mgmatfree_mtf = {'snes_type': 'ksponly',
                 'ksp_type': 'preonly',
                 'mat_type': 'matfree',
                 'pc_type': 'mg',
                 'pc_mg_type': 'full',
                 'mg_coarse_ksp_type': 'preonly',
                 'mg_coarse_pc_type': 'python',
                 'mg_coarse_pc_python_type': 'firedrake.AssembledPC',
                 'mg_coarse_assembled_pc_type': 'lu',
                 'mg_coarse_assembled_pc_factor_mat_solver_type': 'superlu_dist',
                 'mg_coarse_assembled_ksp_monitor': None,
                 # 'mg_coarse_assembled_pc_mat_mumps_icntl_14': 200,
                 'mg_levels_ksp_type': 'chebyshev',
                 'mg_levels_ksp_norm_type': 'unpreconditioned',
                 'mg_levels_ksp_max_it': 3,
                 'mg_levels_pc_type': 'none',
                 'mg_levels_ksp_monitor': None,
                 'ksp_monitor': None,
                 'ksp_norm_type': 'preconditioned',
                 'ksp_monitor_true_residual': None
                 }

mgmatfree_mtf_lessitsonlevels = {'snes_type': 'ksponly',
                                 'ksp_type': 'preonly',
                                 'mat_type': 'matfree',
                                 'pc_type': 'mg',
                                 'pc_mg_type': 'full',
                                 'mg_coarse_ksp_type': 'preonly',
                                 'mg_coarse_pc_type': 'python',
                                 'mg_coarse_pc_python_type': 'firedrake.AssembledPC',
                                 'mg_coarse_assembled_pc_type': 'lu',
                                 'mg_coarse_assembled_pc_factor_mat_solver_type': 'superlu_dist',
                                 'mg_coarse_assembled_ksp_monitor': None,
                                 'mg_levels_ksp_type': 'chebyshev',
                                 'mg_levels_ksp_norm_type': 'unpreconditioned',
                                 'mg_levels_ksp_max_it': 2,
                                 'mg_levels_pc_type': 'none',
                                 'mg_levels_ksp_monitor': None,
                                 'ksp_monitor': None,
                                 'ksp_norm_type': 'preconditioned',
                                 'ksp_monitor_true_residual': None
                                 }

mgmatfree_mtf_moreitsonlevels = {'snes_type': 'ksponly',
                                 'ksp_type': 'preonly',
                                 'mat_type': 'matfree',
                                 'pc_type': 'mg',
                                 'pc_mg_type': 'full',
                                 'mg_coarse_ksp_type': 'preonly',
                                 'mg_coarse_pc_type': 'python',
                                 'mg_coarse_pc_python_type': 'firedrake.AssembledPC',
                                 'mg_coarse_assembled_pc_type': 'lu',
                                 'mg_coarse_assembled_pc_factor_mat_solver_type': 'superlu_dist',
                                 'mg_coarse_assembled_ksp_monitor': None,
                                 'mg_levels_ksp_type': 'chebyshev',
                                 'mg_levels_ksp_norm_type': 'unpreconditioned',
                                 'mg_levels_ksp_max_it': 4,
                                 'mg_levels_pc_type': 'none',
                                 'mg_levels_ksp_monitor': None,
                                 'ksp_monitor': None,
                                 'ksp_norm_type': 'preconditioned',
                                 'ksp_monitor_true_residual': None
                                 }

mgmatfree_mtx = {'snes_type': 'ksponly',
                 'ksp_type': 'preonly',
                 'pc_type': 'python',
                 'pc_python_type': 'firedrake.AssembledPC',
                 'assembled_pc_type': 'mg',
                 'assembled_pc_mg_type': 'full',
                 'assembled_mg_coarse_ksp_type': 'preonly',
                 'assembled_mg_coarse_pc_type': 'python',
                 'assembled_mg_coarse_ksp_type': 'preonly',
                 'assembled_mg_coarse_pc_type': 'lu',
                 'assembled_mg_coarse_pc_factor_mat_solver_type': 'superlu_dist',
                 'assembled_mg_coarse_ksp_monitor': None,
                 'assembled_mg_levels_ksp_type': 'chebyshev',
                 'assembled_mg_levels_ksp_max_it': 3,
                 'assembled_mg_levels_pc_type': 'jacobi',
                 'assembled_mg_levels_ksp_monitor': None,
                 'assembled_mg_levels_ksp_norm_type': 'preconditioned',
                 'assembled_mg_levels_ksp_monitor_true_residual': None,
                 'ksp_monitor': None,
                 'ksp_norm_type': 'unpreconditioned'}

mgmatfree_mtx_higherrtol = {'snes_type': 'ksponly',
                            'ksp_type': 'preonly',
                            'ksp_rtol': 1.e-12,
                            'ksp_atol': 0.0,
                            'pc_type': 'python',
                            'pc_python_type': 'firedrake.AssembledPC',
                            'assembled_pc_type': 'mg',
                            'assembled_pc_mg_type': 'full',
                            'assembled_mg_coarse_ksp_type': 'preonly',
                            'assembled_mg_coarse_ksp_rtol': 1.e-12,
                            'assembled_mg_coarse_pc_type': 'lu',
                            'assembled_mg_coarse_pc_factor_mat_solver_type': 'superlu_dist',
                            'assembled_mg_coarse_ksp_monitor': None,
                            'assembled_mg_levels_ksp_type': 'chebyshev',
                            'assembled_mg_levels_ksp_max_it': 3,
                            'assembled_mg_levels_pc_type': 'jacobi',
                            'assembled_mg_levels_ksp_monitor': None,
                            'assembled_mg_levels_ksp_norm_type': 'preconditioned',
                            'assembled_mg_levels_ksp_monitor_true_residual': None,
                            'ksp_monitor': None,
                            'ksp_norm_type': 'preconditioned'}

mgmatfree_mtx_higherrtol_cleanP1 = {'snes_type': 'ksponly',
                                    'ksp_type': 'cg',
                                    'ksp_rtol': 1.e-8,
                                    'pc_type': 'python',
                                    'pc_python_type': 'firedrake.AssembledPC',
                                    'assembled_pc_type': 'mg',
                                    'assembled_pc_mg_type': 'full',
                                    'assembled_mg_coarse_ksp_type': 'preonly',
                                    'assembled_mg_coarse_ksp_rtol': 1.e-8,
                                    'assembled_mg_coarse_pc_type': 'lu',
                                    'assembled_mg_coarse_pc_factor_mat_solver_type': 'superlu_dist',
                                    'assembled_mg_coarse_ksp_monitor': None,
                                    'assembled_mg_levels_ksp_type': 'chebyshev',
                                    'assembled_mg_levels_ksp_max_it': 3,
                                    'assembled_mg_levels_pc_type': 'jacobi',
                                    'assembled_mg_levels_ksp_convergence_test': "default",
                                    'assembled_mg_levels_ksp_monitor': None,
                                    'assembled_mg_levels_ksp_norm_type': 'preconditioned',
                                    'assembled_mg_levels_ksp_monitor_true_residual': None,
                                    'ksp_monitor': None,
                                    'ksp_norm_type': 'preconditioned'}

mgmatexp = {'ksp_type': 'preonly',
            'pc_type': 'mg',
            'pc_mg_type': 'full',
            'mg_coarse': {'ksp_type': 'preonly',
                          'pc_type': 'lu',
                          'pc_factor_mat_solver_type': 'superlu_dist',
                          'ksp_monitor': None},
            'mg_levels': {'ksp_type': 'chebyshev',
                          'pc_type': 'jacobi',
                          'ksp_max_it': 3,
                          'ksp_monitor': None,
                          'ksp_norm_type': 'preconditioned',
                          'ksp_monitor_true_residual': None}}

mgmatexp_chebynone = {'ksp_type': 'preonly',
                      'pc_type': 'mg',
                      'pc_mg_type': 'full',
                      'mg_coarse': {'ksp_type': 'preonly',
                                    'pc_type': 'lu',
                                    'pc_factor_mat_solver_type': 'superlu_dist',
                                    'ksp_monitor': None},
                      'mg_levels': {'ksp_type': 'chebyshev',
                                    'pc_type': 'none',
                                    'ksp_max_it': 3,
                                    'ksp_monitor': None,
                                    'ksp_norm_type': 'unpreconditioned',
                                    'ksp_monitor_true_residual': None}}

# Params for solves on levels
cheby_jacobi = {'ksp_type': 'chebyshev',
                'ksp_max_it': 3,
                'pc_type': 'jacobi',
                'ksp_monitor': None,
                'ksp_norm_type': 'preconditioned',
                'ksp_monitor_true_residual': None}

cheby_none = {'ksp_type': 'chebyshev',
              'ksp_max_it': 3,
              'pc_type': 'none',
              'ksp_monitor': None,
              'ksp_norm_type': 'unpreconditioned'}

cheby_none_lessitsonlevels = {'ksp_type': 'chebyshev',
                              'ksp_max_it': 2,
                              'pc_type': 'none',
                              'ksp_monitor': None,
                              'ksp_norm_type': 'unpreconditioned'}

cheby_none_moreits = {'ksp_type': 'chebyshev',
                      'ksp_max_it': 10,
                      'pc_type': 'none',
                      'ksp_monitor': None,
                      'ksp_norm_type': 'unpreconditioned'}

cheby_none_moreitsandcg = {'ksp_type': 'chebyshev',
                           'ksp_max_it': 10,
                           "esteig_ksp_type": "cg",
                           "esteig_ksp_norm_type": "unpreconditioned",
                           "esteig_pc_type": "none",
                           # "ksp_chebyshev_esteig": "0.8,0.2,0.0,1.0",
                           # "ksp_chebyshev_esteig_noisy": True,
                           # "ksp_chebyshev_esteig_steps": 8,
                           'pc_type': 'none',
                           'ksp_monitor': None,
                           'ksp_norm_type': 'unpreconditioned',
                           "ksp_convergence_test": "default"}

cheby_assembledjacobi = {'ksp_type': 'chebyshev',
                         'ksp_max_it': 3,
                         'pc_type': 'python',
                         'pc_python_type': 'firedrake.AssembledPC',
                         'assembled_pc_type': 'jacobi',
                         'ksp_monitor': None,
                         'ksp_monitor_true_residual': None}

# Params for GTMG
gt_params_matexp = {'mg_levels': cheby_jacobi,
                    'mg_coarse': mgmatexp}
gt_params_global_matfree = {'mg_coarse': mgmatfree_mtf,
                            'mg_levels': cheby_none,
                            'mat_type': 'matfree'}
gt_params_fully_matfree = {'mg_coarse': mgmatfree_mtf,
                           'mg_levels': cheby_none,
                           'mat_type': 'matfree'}
gt_params_fully_matfree_matexpmg = {'mg_coarse': mgmatfree_mtx,
                                    'mg_levels': cheby_none,
                                    'mat_type': 'matfree'}
gt_params_fully_matfree_matexpmg_assembledjacobi = {'mg_coarse': mgmatfree_mtx,
                                                    'mg_levels': cheby_assembledjacobi,
                                                    'mat_type': 'matfree'}
gt_params_global_matfree_lessitsonlevels = {'mg_coarse': mgmatfree_mtf_lessitsonlevels,
                                            'mg_levels': cheby_none,
                                            'mat_type': 'matfree'}
gt_params_global_matfree_moreitsonlevels = {'mg_coarse': mgmatfree_mtf_moreitsonlevels,
                                            'mg_levels': cheby_none,
                                            'mat_type': 'matfree'}
gt_params_global_matfree_matexpmg = {'mg_coarse': mgmatfree_mtx,
                                     'mg_levels': cheby_none,
                                     'mat_type': 'matfree'}
gt_params_global_matfree_matexpmg_higherrtol = {'mg_coarse': mgmatfree_mtx_higherrtol,
                                                'mg_levels': cheby_none,
                                                'mat_type': 'matfree'}
gt_params_global_matfree_matexpmg_higherrtol_cleanP1 = {'mg_coarse': mgmatfree_mtx_higherrtol_cleanP1,
                                                        'mg_levels': cheby_none,
                                                        'mat_type': 'matfree'}
gt_params_global_matfree_matexpmg_higherrtol_cleanP1_moreits = {'mg_coarse': mgmatfree_mtx_higherrtol_cleanP1,
                                                                'mg_levels': cheby_none_moreits,
                                                                'mat_type': 'matfree'}
gt_params_global_matfree_matexpmg_higherrtol_cleanP1_moreitsandcg = {'mg_coarse': mgmatfree_mtx_higherrtol_cleanP1,
                                                                     'mg_levels': cheby_none_moreitsandcg,
                                                                     'mat_type': 'matfree'}

gt_params_global_matfree_matexpmg_assembledjacobi = {'mg_coarse': mgmatfree_mtx,
                                                     'mg_levels': cheby_assembledjacobi,
                                                     'mat_type': 'matfree'}


# 2) FULL PARAMS
# Matrix explicit, direct hybridization
hybridization_lu_params = {'mat_type': 'matfree',
                           'ksp_type': 'preonly',
                           'pc_type': 'python',
                           'pc_python_type': 'firedrake.HybridizationPC',
                           'hybridization': {'ksp_type': 'preonly', 'pc_type': 'lu', 'pc_factor_mat_solver_type': 'superlu_dist',
                                             'ksp_rtol': 1.e-6,
                                             'ksp_atol': 1.e-6,
                                             'ksp_monitor': None},
                           'ksp_view': None}

hybridization_cg_params = {'mat_type': 'matfree',
                           'ksp_type': 'preonly',
                           'pc_type': 'python',
                           'pc_python_type': 'firedrake.HybridizationPC',
                           'hybridization': {'ksp_type': 'cg', 'pc_type': 'none',
                                             'ksp_rtol': 1.e-6,
                                             'ksp_atol': 1.e-6,
                                             'ksp_monitor': None},
                           'ksp_view': None}

# Hyridization, globally matfree with CG, used in Thomas' matrix-free hybridization test
hybridization_fully_matfree_cg = {'mat_type': 'matfree',
                                  'ksp_type': 'preonly',
                                  'pc_type': 'python',
                                  'pc_python_type': 'firedrake.HybridizationPC',
                                  'hybridization': {'ksp_type': 'cg',
                                                    'pc_type': 'none',
                                                                'ksp_rtol': 1.e-6,
                                                                'ksp_atol': 1.e-6,
                                                    'mat_type': 'matfree',
                                                    'localsolve': {'ksp_type': 'preonly',
                                                                   'mat_type': 'matfree',  # local-matfree!
                                                                   'pc_type': 'fieldsplit',
                                                                   'pc_fieldsplit_type': 'schur'},
                                                    'ksp_view': None,
                                                    'ksp_monitor': None}}

# Hyridization, globally matfree with CG, used in Thomas' matrix-free hybridization test
hybridization_global_matfree_cg = {'mat_type': 'matfree',
                                   'ksp_type': 'preonly',
                                   'pc_type': 'python',
                                   'pc_python_type': 'firedrake.HybridizationPC',
                                   'hybridization': {'ksp_type': 'cg',
                                                     'pc_type': 'none',
                                                                'ksp_rtol': 1.e-6,
                                                                'ksp_atol': 1.e-6,
                                                     'mat_type': 'matfree',
                                                     'ksp_view': None,
                                                     'ksp_monitor': None}}

# These are the tests used for Jacks GTMG test in the Firedrake test suite
gtmg_matexpl_params = {'mat_type': 'matfree',
                       'ksp_type': 'preonly',
                       'pc_type': 'python',
                       'pc_python_type': 'firedrake.HybridizationPC',
                       'hybridization': {'ksp_type': 'cg',
                                         'pc_type': 'python',
                                         'ksp_rtol': 1.e-6,
                                         'ksp_atol': 1.e-6,
                                         'pc_python_type': 'firedrake.GTMGPC',
                                         'gt': {'mg_levels': cheby_jacobi,
                                                'mg_coarse': mgmatexp},
                                         'ksp_view': None,
                                         'ksp_monitor': None}}

# These are the tests used for Jacks GTMG test in the Firedrake test suite
gtmg_matexpl_params_chebynone = {'mat_type': 'matfree',
                                 'ksp_type': 'preonly',
                                 'pc_type': 'python',
                                 'pc_python_type': 'firedrake.HybridizationPC',
                                 'hybridization': {'ksp_type': 'cg',
                                                   'pc_type': 'python',
                                                   'ksp_rtol': 1.e-6,
                                                   'ksp_atol': 1.e-6,
                                                   'pc_python_type': 'firedrake.GTMGPC',
                                                   'gt': {'mg_levels': cheby_none,
                                                          'mg_coarse': mgmatexp_chebynone},
                                                   'ksp_view': None,
                                                   'ksp_monitor': None}}

gtmg_matexpl_params_maxitscg = {'mat_type': 'matfree',
                                'ksp_type': 'preonly',
                                'pc_type': 'python',
                                'pc_python_type': 'firedrake.HybridizationPC',
                                'hybridization': {'ksp_type': 'cg',
                                                  'pc_type': 'python',
                                                  'ksp_rtol': 1.e-6,
                                                  'ksp_atol': 1.e-6,
                                                  'ksp_max_it': 10,
                                                  'pc_python_type': 'firedrake.GTMGPC',
                                                  'gt': {'mg_levels': cheby_jacobi,
                                                         'mg_coarse': mgmatexp},
                                                  'ksp_view': None,
                                                  'ksp_monitor': None}}

# These are the tests used for Jacks GTMG test in the Firedrake test suite
# but the Schur complement in the trace solve is nested
gtmg_matexpl_nested_schur_params = {'mat_type': 'matfree',
                                    'ksp_type': 'preonly',
                                    'pc_type': 'python',
                                    'pc_python_type': 'firedrake.HybridizationPC',
                                    'hybridization': {'ksp_type': 'cg',
                                                      'pc_type': 'python',
                                                      'ksp_rtol': 1.e-6,
                                                      'ksp_atol': 1.e-6,
                                                      # nested schur option
                                                      'localsolve': {'ksp_type': 'preonly',
                                                                     'pc_type': 'fieldsplit',
                                                                     'pc_fieldsplit_type': 'schur'},
                                                      'pc_python_type': 'firedrake.GTMGPC',
                                                      'gt': {'mg_levels': cheby_jacobi,
                                                             'mg_coarse': mgmatexp}},
                                    'ksp_view': None,
                                    'ksp_monitor': None}


gtmg_matexpl_nested_schur_params_fgmres = {'mat_type': 'matfree',
                                           'ksp_type': 'preonly',
                                           'pc_type': 'python',
                                           'pc_python_type': 'firedrake.HybridizationPC',
                                           'hybridization': {'ksp_type': 'fgmres',
                                                             'pc_type': 'python',
                                                             'ksp_rtol': 1.e-6,
                                                             'ksp_atol': 1.e-6,
                                                             # nested schur option
                                                             'localsolve': {'ksp_type': 'preonly',
                                                                            'pc_type': 'fieldsplit',
                                                                            'pc_fieldsplit_type': 'schur'},
                                                             'pc_python_type': 'firedrake.GTMGPC',
                                                             'gt': {'mg_levels': cheby_jacobi,
                                                                    'mg_coarse': mgmatexp}},
                                           'ksp_view': None,
                                           'ksp_monitor': None}


gtmg_matexpl_nested_schur_params_chebynone = {'mat_type': 'matfree',
                                              'ksp_type': 'preonly',
                                              'pc_type': 'python',
                                              'pc_python_type': 'firedrake.HybridizationPC',
                                              'hybridization': {'ksp_type': 'cg',
                                                                'pc_type': 'python',
                                                                'ksp_rtol': 1.e-6,
                                                                'ksp_atol': 1.e-6,
                                                                # nested schur option
                                                                'localsolve': {'ksp_type': 'preonly',
                                                                               'pc_type': 'fieldsplit',
                                                                               'pc_fieldsplit_type': 'schur'},
                                                                'pc_python_type': 'firedrake.GTMGPC',
                                                                'gt': {'mg_levels': cheby_none,
                                                                       'mg_coarse': mgmatexp}},
                                              'ksp_view': None,
                                              'ksp_monitor': None}

# These are the tests used for Jacks GTMG test in the Firedrake test suite
# with globally matrix-free solves on the levels
gtmg_global_matfree_params = {'snes_type': 'ksponly',
                              'mat_type': 'matfree',
                              'ksp_type': 'preonly',
                              'pc_type': 'python',
                              'pc_python_type': 'firedrake.HybridizationPC',
                              'hybridization': {'ksp_type': 'cg',
                                                'pc_type': 'python',
                                                # global matfree
                                                'mat_type': 'matfree',
                                                'pc_python_type': 'firedrake.GTMGPC',
                                                'ksp_rtol': 1.e-6,
                                                'ksp_atol': 1.e-6,
                                                'gt': gt_params_global_matfree,
                                                'ksp_view': None,
                                                'ksp_monitor': None,
                                                'ksp_converged_reason': None}}

gtmg_global_matfree_params_maxitscg = {'snes_type': 'ksponly',
                                       'mat_type': 'matfree',
                                       'ksp_type': 'preonly',
                                       'pc_type': 'python',
                                       'pc_python_type': 'firedrake.HybridizationPC',
                                       'hybridization': {'ksp_type': 'cg',
                                                         'pc_type': 'python',
                                                         # global matfree
                                                         'mat_type': 'matfree',
                                                         'pc_python_type': 'firedrake.GTMGPC',
                                                         'ksp_rtol': 1.e-6,
                                                         'ksp_atol': 1.e-6,
                                                         'ksp_max_it': 10,
                                                         'gt': gt_params_global_matfree,
                                                         'ksp_view': None,
                                                         'ksp_monitor': None}}


# These are the tests used for Jacks GTMG test in the Firedrake test suite
# with globally matrix-free solves on the levels and a nesting of schur complements on the trace solve
gtmg_global_matfree_nested_schur_params = {'snes_type': 'ksponly',
                                           'mat_type': 'matfree',
                                           'ksp_type': 'preonly',
                                           'pc_type': 'python',
                                           'pc_python_type': 'firedrake.HybridizationPC',
                                           'hybridization': {'ksp_type': 'cg',
                                                             'pc_type': 'python',
                                                             # global matfree
                                                             'mat_type': 'matfree',
                                                             # nested schur option, but not locally matfree!
                                                             'localsolve': {'ksp_type': 'preonly',
                                                                            # 'mat_type': 'matfree',
                                                                            'pc_type': 'fieldsplit',
                                                                            'pc_fieldsplit_type': 'schur'},
                                                             'ksp_rtol': 1.e-6,
                                                             'ksp_atol': 1.e-6,
                                                             'pc_python_type': 'firedrake.GTMGPC',
                                                             'gt': gt_params_global_matfree,
                                                             'ksp_view': None,
                                                             'ksp_monitor': None}}


gtmg_global_matfree_nested_schur_params_fgmres = {'snes_type': 'ksponly',
                                                  'mat_type': 'matfree',
                                                  'ksp_type': 'preonly',
                                                  'pc_type': 'python',
                                                  'pc_python_type': 'firedrake.HybridizationPC',
                                                  'hybridization': {'ksp_type': 'fgmres',
                                                                    'pc_type': 'python',
                                                                    # global matfree
                                                                    'mat_type': 'matfree',
                                                                    # nested schur option, but not locally matfree!
                                                                    'localsolve': {'ksp_type': 'preonly',
                                                                                   # 'mat_type': 'matfree',
                                                                                   'pc_type': 'fieldsplit',
                                                                                   'pc_fieldsplit_type': 'schur'},
                                                                    'ksp_rtol': 1.e-6,
                                                                    'ksp_atol': 1.e-6,
                                                                    'pc_python_type': 'firedrake.GTMGPC',
                                                                    'gt': gt_params_global_matfree,
                                                                    'ksp_view': None,
                                                                    'ksp_monitor': None,
                                                                    'ksp_converged_reason': None}}


gtmg_global_matfree_params_matexpmg_nested_schur_fgmres = {'snes_type': 'ksponly',
                                                           'mat_type': 'matfree',
                                                           'ksp_type': 'preonly',
                                                           'pc_type': 'python',
                                                           'pc_python_type': 'firedrake.HybridizationPC',
                                                           'hybridization': {'ksp_type': 'fgmres',
                                                                             'pc_type': 'python',
                                                                             # global matfree
                                                                             'mat_type': 'matfree',
                                                                             # nested schur option, but not locally matfree!
                                                                             'localsolve': {'ksp_type': 'preonly',
                                                                                            # 'mat_type': 'matfree',
                                                                                            'pc_type': 'fieldsplit',
                                                                                            'pc_fieldsplit_type': 'schur'},
                                                                             'ksp_rtol': 1.e-6,
                                                                             'ksp_atol': 1.e-6,
                                                                             'pc_python_type': 'firedrake.GTMGPC',
                                                                             'gt': gt_params_global_matfree_matexpmg,
                                                                             'ksp_view': None,
                                                                             'ksp_monitor': None,
                                                                             'ksp_converged_reason': None}}


# Fully matrix-free GTMG
# We need nested schur for local matfree
gtmg_fully_matfree_params = {'snes_type': 'ksponly',
                             'mat_type': 'matfree',
                             'ksp_type': 'preonly',
                             'pc_type': 'python',
                             'pc_python_type': 'firedrake.HybridizationPC',
                             'hybridization': {'ksp_type': 'fgmres',
                                               'pc_type': 'python',
                                               'mat_type': 'matfree',
                                               'ksp_rtol': 1.e-6,
                                               'ksp_atol': 1.e-6,
                                               'localsolve': {'ksp_type': 'preonly',
                                                              'mat_type': 'matfree',  # local-matfree!
                                                              'pc_type': 'fieldsplit',
                                                              'pc_fieldsplit_type': 'schur',
                                                              'fieldsplit_0': {'ksp_rtol': 1.e-12,
                                                                               'ksp_atol': 1.e-12},
                                                              'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                               'ksp_atol': 1.e-10},
                                                              },
                                               'pc_python_type': 'firedrake.GTMGPC',
                                               'gt': gt_params_fully_matfree,
                                               'ksp_view': None,
                                               'ksp_monitor': None,
                                               'ksp_converged_reason': None}}


gtmg_fully_matfree_params_fgmres = {'snes_type': 'ksponly',
                                    'mat_type': 'matfree',
                                    'ksp_type': 'preonly',
                                    'pc_type': 'python',
                                    'pc_python_type': 'firedrake.HybridizationPC',
                                    'hybridization': {'ksp_type': 'fgmres',
                                                      'pc_type': 'python',
                                                      'ksp_rtol': 1.e-6,
                                                      'ksp_atol': 1.e-6,
                                                      'localsolve': {'ksp_type': 'preonly',
                                                                     'mat_type': 'matfree',  # local-matfree!
                                                                     'pc_type': 'fieldsplit',
                                                                     'pc_fieldsplit_type': 'schur',
                                                                     'fieldsplit_0': {'ksp_rtol': 1.e-12,
                                                                                      'ksp_atol': 1.e-12},
                                                                     'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                      'ksp_atol': 1.e-10}},
                                                      'pc_python_type': 'firedrake.GTMGPC',
                                                      'gt': gt_params_fully_matfree,
                                                      'ksp_view': None,
                                                      'ksp_monitor': None,
                                                      'ksp_converged_reason': None}}


gtmg_fully_matfree_params_matexpmg = {'snes_type': 'ksponly',
                                      'mat_type': 'matfree',
                                      'ksp_type': 'preonly',
                                      'pc_type': 'python',
                                      'pc_python_type': 'firedrake.HybridizationPC',
                                      'hybridization': {'ksp_type': 'cg',
                                                        'pc_type': 'python',
                                                        'ksp_rtol': 1.e-6,
                                                        'ksp_atol': 1.e-6,
                                                        'localsolve': {'ksp_type': 'preonly',
                                                                       'mat_type': 'matfree',  # local-matfree!
                                                                       'pc_type': 'fieldsplit',
                                                                       'pc_fieldsplit_type': 'schur',
                                                                       'fieldsplit_0': {'ksp_rtol': 1.e-12,
                                                                                        'ksp_atol': 1.e-12},
                                                                       'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                        'ksp_atol': 1.e-10}},
                                                        'pc_python_type': 'firedrake.GTMGPC',
                                                        'gt': gt_params_fully_matfree_matexpmg,
                                                        'ksp_view': None,
                                                        'ksp_monitor': None,
                                                        'ksp_converged_reason': None}}


gtmg_fully_matfree_params_matexpmg_fgmres = {'snes_type': 'ksponly',
                                             'mat_type': 'matfree',
                                             'ksp_type': 'preonly',
                                             'pc_type': 'python',
                                             'pc_python_type': 'firedrake.HybridizationPC',
                                             'hybridization': {'ksp_type': 'fgmres',
                                                               'pc_type': 'python',
                                                               'ksp_rtol': 1.e-6,
                                                               'ksp_atol': 1.e-6,
                                                               'localsolve': {'ksp_type': 'preonly',
                                                                              'mat_type': 'matfree',  # local-matfree!
                                                                              'pc_type': 'fieldsplit',
                                                                              'pc_fieldsplit_type': 'schur',
                                                                              'fieldsplit_0': {'ksp_rtol': 1.e-12,
                                                                                               'ksp_atol': 1.e-12},
                                                                              'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                               'ksp_atol': 1.e-10}},
                                                               'pc_python_type': 'firedrake.GTMGPC',
                                                               'gt': gt_params_fully_matfree_matexpmg,
                                                               'ksp_view': None,
                                                               'ksp_monitor': None,
                                                               'ksp_converged_reason': None}}


gtmg_fully_matfree_params_matexpmg_fgmres_assembledjacobi = {'snes_type': 'ksponly',
                                                             'mat_type': 'matfree',
                                                             'ksp_type': 'preonly',
                                                             'pc_type': 'python',
                                                             'pc_python_type': 'firedrake.HybridizationPC',
                                                             'hybridization': {'ksp_type': 'fgmres',
                                                                               'pc_type': 'python',
                                                                               'mat_type': 'matfree',
                                                                               'ksp_rtol': 1.e-6,
                                                                               'ksp_atol': 1.e-6,
                                                                               'localsolve': {'ksp_type': 'preonly',
                                                                                              'mat_type': 'matfree',  # local-matfree!
                                                                                              'pc_type': 'fieldsplit',
                                                                                              'pc_fieldsplit_type': 'schur',
                                                                                              'fieldsplit_0': {'ksp_rtol': 1.e-12,
                                                                                                               'ksp_atol': 1.e-12},
                                                                                              'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                                               'ksp_atol': 1.e-10}},
                                                                               'pc_python_type': 'firedrake.GTMGPC',
                                                                               'gt': gt_params_fully_matfree_matexpmg_assembledjacobi,
                                                                               'ksp_view': None,
                                                                               'ksp_monitor': None,
                                                                               'ksp_converged_reason': None}}


gtmg_global_matfree_params_lessitsonlevels = {'snes_type': 'ksponly',
                                              'mat_type': 'matfree',
                                              'ksp_type': 'preonly',
                                              'pc_type': 'python',
                                              'pc_python_type': 'firedrake.HybridizationPC',
                                              'hybridization': {'ksp_type': 'cg',
                                                                'pc_type': 'python',
                                                                'mat_type': 'matfree',
                                                                'ksp_rtol': 1.e-6,
                                                                'ksp_atol': 1.e-6,
                                                                'pc_python_type': 'firedrake.GTMGPC',
                                                                'gt': gt_params_global_matfree_lessitsonlevels,
                                                                'ksp_view': None,
                                                                'ksp_monitor': None}}

gtmg_global_matfree_params_moreitsonlevels = {'snes_type': 'ksponly',
                                              'mat_type': 'matfree',
                                              'ksp_type': 'preonly',
                                              'pc_type': 'python',
                                              'pc_python_type': 'firedrake.HybridizationPC',
                                              'hybridization': {'ksp_type': 'cg',
                                                                'pc_type': 'python',
                                                                'mat_type': 'matfree',
                                                                'ksp_rtol': 1.e-6,
                                                                'ksp_atol': 1.e-6,
                                                                'pc_python_type': 'firedrake.GTMGPC',
                                                                'gt': gt_params_global_matfree_moreitsonlevels,
                                                                'ksp_view': None,
                                                                'ksp_monitor': None}}


gtmg_global_matfree_params_matexpmg = {'snes_type': 'ksponly',
                                       'mat_type': 'matfree',
                                       'ksp_type': 'preonly',
                                       'pc_type': 'python',
                                       'pc_python_type': 'firedrake.HybridizationPC',
                                       'hybridization': {'ksp_type': 'cg',
                                                         'pc_type': 'python',
                                                         'mat_type': 'matfree',
                                                         'ksp_rtol': 1.e-6,
                                                         'ksp_atol': 1.e-6,
                                                         'pc_python_type': 'firedrake.GTMGPC',
                                                         'gt': gt_params_global_matfree_matexpmg,
                                                         'ksp_view': None,
                                                         'ksp_monitor': None}}

gtmg_global_matfree_params_matexpmg_higherrtol = {'snes_type': 'ksponly',
                                                  'mat_type': 'matfree',
                                                  'ksp_type': 'preonly',
                                                  'pc_type': 'python',
                                                  'pc_python_type': 'firedrake.HybridizationPC',
                                                  'hybridization': {'ksp_type': 'cg',
                                                                    'pc_type': 'python',
                                                                    'mat_type': 'matfree',
                                                                    'ksp_rtol': 1.e-6,
                                                                    'ksp_atol': 1.e-6,
                                                                    'pc_python_type': 'firedrake.GTMGPC',
                                                                    'gt': gt_params_global_matfree_matexpmg_higherrtol,
                                                                    'ksp_view': None,
                                                                    'ksp_monitor': None}}

gtmg_global_matfree_params_matexpmg_higherrtol_cleanP1 = {'snes_type': 'ksponly',
                                                          'mat_type': 'matfree',
                                                          'ksp_type': 'preonly',
                                                          'pc_type': 'python',
                                                          'pc_python_type': 'firedrake.HybridizationPC',
                                                          'hybridization': {'ksp_type': 'cg',
                                                                            'pc_type': 'python',
                                                                            'mat_type': 'matfree',
                                                                            'ksp_rtol': 1.e-6,
                                                                            'ksp_atol': 1.e-6,
                                                                            'pc_python_type': 'firedrake.GTMGPC',
                                                                            'gt': gt_params_global_matfree_matexpmg_higherrtol_cleanP1,
                                                                            'ksp_view': None,
                                                                            'ksp_monitor': None}}

gtmg_global_matfree_params_matexpmg_higherrtol_cleanP1_moreits = {'snes_type': 'ksponly',
                                                                  'mat_type': 'matfree',
                                                                  'ksp_type': 'preonly',
                                                                  'pc_type': 'python',
                                                                  'pc_python_type': 'firedrake.HybridizationPC',
                                                                  'hybridization': {'ksp_type': 'cg',
                                                                                    'pc_type': 'python',
                                                                                    'mat_type': 'matfree',
                                                                                    'ksp_rtol': 1.e-6,
                                                                                    'ksp_atol': 1.e-6,
                                                                                    'pc_python_type': 'firedrake.GTMGPC',
                                                                                    'gt': gt_params_global_matfree_matexpmg_higherrtol_cleanP1_moreits,
                                                                                    'ksp_view': None,
                                                                                    'ksp_monitor': None}}

gtmg_global_matfree_params_matexpmg_higherrtol_cleanP1_moreitsandcg = {'snes_type': 'ksponly',
                                                                       'mat_type': 'matfree',
                                                                       'ksp_type': 'preonly',
                                                                       'pc_type': 'python',
                                                                       'pc_python_type': 'firedrake.HybridizationPC',
                                                                       'hybridization': {'ksp_type': 'cg',
                                                                                         'pc_type': 'python',
                                                                                         'mat_type': 'matfree',
                                                                                         'ksp_rtol': 1.e-6,
                                                                                         'ksp_atol': 1.e-6,
                                                                                         'pc_python_type': 'firedrake.GTMGPC',
                                                                                         'gt': gt_params_global_matfree_matexpmg_higherrtol_cleanP1_moreitsandcg,
                                                                                         'ksp_view': None,
                                                                                         'ksp_monitor': None}}


gtmg_global_matfree_params_matexpmg_assembledjacobi = {'snes_type': 'ksponly',
                                                       'mat_type': 'matfree',
                                                       'ksp_type': 'preonly',
                                                       'pc_type': 'python',
                                                       'pc_python_type': 'firedrake.HybridizationPC',
                                                       'hybridization': {'ksp_type': 'cg',
                                                                         'pc_type': 'python',
                                                                         'mat_type': 'matfree',
                                                                         'ksp_rtol': 1.e-6,
                                                                         'ksp_atol': 1.e-6,
                                                                         'pc_python_type': 'firedrake.GTMGPC',
                                                                         'gt': gt_params_global_matfree_matexpmg_assembledjacobi,
                                                                         'ksp_view': None,
                                                                         'ksp_monitor': None}}


gtmg_global_matfree_params_matexpmg_assembledjacobi_fgmres = {'snes_type': 'ksponly',
                                                              'mat_type': 'matfree',
                                                              'ksp_type': 'preonly',
                                                              'pc_type': 'python',
                                                              'pc_python_type': 'firedrake.HybridizationPC',
                                                              'hybridization': {'ksp_type': 'fgmres',
                                                                                'pc_type': 'python',
                                                                                'mat_type': 'matfree',
                                                                                'ksp_rtol': 1.e-6,
                                                                                'ksp_atol': 1.e-6,
                                                                                'pc_python_type': 'firedrake.GTMGPC',
                                                                                'gt': gt_params_global_matfree_matexpmg_assembledjacobi,
                                                                                'ksp_view': None,
                                                                                'ksp_monitor': None}}

gtmg_global_matfree_params_matexpmg_assembledjacobi_cg = {'snes_type': 'ksponly',
                                                          'mat_type': 'matfree',
                                                          'ksp_type': 'preonly',
                                                          'pc_type': 'python',
                                                          'pc_python_type': 'firedrake.HybridizationPC',
                                                          'hybridization': {'ksp_type': 'cg',
                                                                            'pc_type': 'python',
                                                                            'mat_type': 'matfree',
                                                                            'ksp_rtol': 1.e-6,
                                                                            'ksp_atol': 1.e-6,
                                                                            'pc_python_type': 'firedrake.GTMGPC',
                                                                            'gt': gt_params_global_matfree_matexpmg_assembledjacobi,
                                                                            'ksp_view': None,
                                                                            'ksp_monitor': None}}

gtmg_fully_matfree_params_maxitscg = {'snes_type': 'ksponly',
                                      'mat_type': 'matfree',
                                      'ksp_type': 'preonly',
                                      'pc_type': 'python',
                                      'pc_python_type': 'firedrake.HybridizationPC',
                                      'hybridization': {'ksp_type': 'cg',
                                                        'pc_type': 'python',
                                                        'mat_type': 'matfree',
                                                                    'ksp_rtol': 1.e-6,
                                                                    'ksp_atol': 1.e-6,
                                                        'ksp_max_it': 10,
                                                        'localsolve': {'ksp_type': 'preonly',
                                                                       'mat_type': 'matfree',  # local-matfree!
                                                                       'pc_type': 'fieldsplit',
                                                                       'pc_fieldsplit_type': 'schur'},
                                                        'pc_python_type': 'firedrake.GTMGPC',
                                                        'gt': gt_params_fully_matfree,
                                                        'ksp_view': None,
                                                        'ksp_monitor': None}}

gtmg_fully_matfree_params_fs0_cg_jacobi = {'snes_type': 'ksponly',
                                           'mat_type': 'matfree',
                                           'ksp_type': 'preonly',
                                           'pc_type': 'python',
                                           'pc_python_type': 'firedrake.HybridizationPC',
                                           'hybridization': {'ksp_type': 'cg',
                                                             'pc_type': 'python',
                                                             'mat_type': 'matfree',
                                                             'ksp_rtol': 1.e-6,
                                                             'ksp_atol': 1.e-6,
                                                             'ksp_max_it': 10,
                                                             'localsolve': {'ksp_type': 'preonly',
                                                                            'mat_type': 'matfree',  # local-matfree!
                                                                            'pc_type': 'fieldsplit',
                                                                            'pc_fieldsplit_type': 'schur',
                                                                            'fieldsplit_0': {'ksp_type': 'default',
                                                                                             'pc_type': 'jacobi',
                                                                                             'ksp_rtol': 1.e-12,
                                                                                             'ksp_atol': 1.e-12},
                                                                            'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                             'ksp_atol': 1.e-10}},
                                                             'pc_python_type': 'firedrake.GTMGPC',
                                                             'gt': gt_params_fully_matfree,
                                                             'ksp_view': None,
                                                             'ksp_monitor': None,
                                                             'ksp_converged_reason': None}}

gtmg_fully_matfree_params_fs0_cg_jacobi_fgmres = {'snes_type': 'ksponly',
                                                  'mat_type': 'matfree',
                                                  'ksp_type': 'preonly',
                                                  'pc_type': 'python',
                                                  'pc_python_type': 'firedrake.HybridizationPC',
                                                  'hybridization': {'ksp_type': 'fgmres',
                                                                    'pc_type': 'python',
                                                                    'mat_type': 'matfree',
                                                                    'ksp_rtol': 1.e-6,
                                                                    'ksp_atol': 1.e-6,
                                                                    'localsolve': {'ksp_type': 'preonly',
                                                                                   'mat_type': 'matfree',  # local-matfree!
                                                                                   'pc_type': 'fieldsplit',
                                                                                   'pc_fieldsplit_type': 'schur',
                                                                                   'fieldsplit_0': {'ksp_type': 'default',
                                                                                                    'pc_type': 'jacobi',
                                                                                                    'ksp_rtol': 1.e-12,
                                                                                                    'ksp_atol': 1.e-12},
                                                                                   'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                                    'ksp_atol': 1.e-10}},
                                                                    'pc_python_type': 'firedrake.GTMGPC',
                                                                    'gt': gt_params_fully_matfree,
                                                                    'ksp_view': None,
                                                                    'ksp_monitor': None,
                                                                    'ksp_converged_reason': None}}


gtmg_fully_matfree_params_matexpmg_assembledjacobi_fs0_cg_jacobi_fgmres = {'snes_type': 'ksponly',
                                                                           'mat_type': 'matfree',
                                                                           'ksp_type': 'preonly',
                                                                           'pc_type': 'python',
                                                                           'pc_python_type': 'firedrake.HybridizationPC',
                                                                           'hybridization': {'ksp_type': 'fgmres',
                                                                                             'pc_type': 'python',
                                                                                             'mat_type': 'matfree',
                                                                                             'ksp_rtol': 1.e-6,
                                                                                             'ksp_atol': 1.e-6,
                                                                                             'localsolve': {'ksp_type': 'preonly',
                                                                                                            'mat_type': 'matfree',  # local-matfree!
                                                                                                            'pc_type': 'fieldsplit',
                                                                                                            'pc_fieldsplit_type': 'schur',
                                                                                                            'fieldsplit_0': {'ksp_type': 'default',
                                                                                                                             'pc_type': 'jacobi',
                                                                                                                             'ksp_rtol': 1.e-12,
                                                                                                                             'ksp_atol': 1.e-12},
                                                                                                            'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                                                             'ksp_atol': 1.e-10}},
                                                                                             'pc_python_type': 'firedrake.GTMGPC',
                                                                                             'gt': gt_params_fully_matfree_matexpmg_assembledjacobi,
                                                                                             'ksp_view': None,
                                                                                             'ksp_monitor': None,
                                                                                             'ksp_converged_reason': None}}
gtmg_fully_matfree_params_matexpmg_assembledjacobi_cg = {'snes_type': 'ksponly',
                                                         'mat_type': 'matfree',
                                                         'ksp_type': 'preonly',
                                                         'pc_type': 'python',
                                                         'pc_python_type': 'firedrake.HybridizationPC',
                                                         'hybridization': {'ksp_type': 'cg',
                                                                           'pc_type': 'python',
                                                                           'mat_type': 'matfree',
                                                                           'ksp_rtol': 1.e-6,
                                                                           'ksp_atol': 1.e-6,
                                                                           'localsolve': {'ksp_type': 'preonly',
                                                                                          'mat_type': 'matfree',  # local-matfree!
                                                                                          'pc_type': 'fieldsplit',
                                                                                          'pc_fieldsplit_type': 'schur',
                                                                                          'fieldsplit_0': {'ksp_rtol': 1.e-12,
                                                                                                           'ksp_atol': 1.e-12},
                                                                                          'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                                           'ksp_atol': 1.e-10}},
                                                                           'pc_python_type': 'firedrake.GTMGPC',
                                                                           'gt': gt_params_fully_matfree_matexpmg_assembledjacobi,
                                                                           'ksp_view': None,
                                                                           'ksp_monitor': None,
                                                                           'ksp_converged_reason': None}}

gtmg_fully_matfree_params_matexpmg_assembledjacobi_fs0_cg_jacobi_fgmres_lesstolonS = {'snes_type': 'ksponly',
                                                                                      'mat_type': 'matfree',
                                                                                      'ksp_type': 'preonly',
                                                                                      'pc_type': 'python',
                                                                                      'pc_python_type': 'firedrake.HybridizationPC',
                                                                                      'hybridization': {'ksp_type': 'fgmres',
                                                                                                        'pc_type': 'python',
                                                                                                        'mat_type': 'matfree',
                                                                                                        'ksp_rtol': 1.e-6,
                                                                                                        'ksp_atol': 1.e-6,
                                                                                                        'localsolve': {'ksp_type': 'preonly',
                                                                                                                       'mat_type': 'matfree',  # local-matfree!
                                                                                                                       'pc_type': 'fieldsplit',
                                                                                                                       'pc_fieldsplit_type': 'schur',
                                                                                                                       'fieldsplit_0': {'ksp_type': 'default',
                                                                                                                                        'pc_type': 'jacobi',
                                                                                                                                        'ksp_rtol': 1.e-12,
                                                                                                                                        'ksp_atol': 1.e-12},
                                                                                                                       'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                                                                        'ksp_atol': 1.e-10}},
                                                                                                        'pc_python_type': 'firedrake.GTMGPC',
                                                                                                        'gt': gt_params_fully_matfree_matexpmg_assembledjacobi,
                                                                                                        'ksp_view': None,
                                                                                                        'ksp_monitor': None,
                                                                                                        'ksp_converged_reason': None}}


gtmg_fully_matfree_params_matexpmg_assembledjacobi_fs0_cg_jacobi_fgmres_lesstolonSbutbitmore = {'snes_type': 'ksponly',
                                                                                                'mat_type': 'matfree',
                                                                                                'ksp_type': 'preonly',
                                                                                                'pc_type': 'python',
                                                                                                'pc_python_type': 'firedrake.HybridizationPC',
                                                                                                'hybridization': {'ksp_type': 'fgmres',
                                                                                                                  'pc_type': 'python',
                                                                                                                  'ksp_rtol': 1.e-6,
                                                                                                                  'ksp_atol': 1.e-6,
                                                                                                                  'localsolve': {'ksp_type': 'preonly',
                                                                                                                                 'mat_type': 'matfree',  # local-matfree!
                                                                                                                                 'pc_type': 'fieldsplit',
                                                                                                                                 'pc_fieldsplit_type': 'schur',
                                                                                                                                 'fieldsplit_0': {'ksp_type': 'default',
                                                                                                                                                  'pc_type': 'jacobi',
                                                                                                                                                  'ksp_rtol': 1.e-12,
                                                                                                                                                  'ksp_atol': 1.e-12},
                                                                                                                                 'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                                                                                  'ksp_atol': 1.e-10}},
                                                                                                                  'pc_python_type': 'firedrake.GTMGPC',
                                                                                                                  'gt': gt_params_fully_matfree_matexpmg_assembledjacobi,
                                                                                                                  'ksp_view': None,
                                                                                                                  'ksp_monitor': None,
                                                                                                                  'ksp_converged_reason': None}}

gtmg_fully_matfree_params_matexpmg_assembledjacobi_fs0_cg_jacobi_fgmres_moretol = {'snes_type': 'ksponly',
                                                                                   'mat_type': 'matfree',
                                                                                   'ksp_type': 'preonly',
                                                                                   'pc_type': 'python',
                                                                                   'pc_python_type': 'firedrake.HybridizationPC',
                                                                                   'hybridization': {'ksp_type': 'fgmres',
                                                                                                     'pc_type': 'python',
                                                                                                     'mat_type': 'matfree',
                                                                                                     'ksp_rtol': 1.e-6,
                                                                                                     'ksp_atol': 1.e-6,
                                                                                                     'localsolve': {'ksp_type': 'preonly',
                                                                                                                    'mat_type': 'matfree',  # local-matfree!
                                                                                                                    'pc_type': 'fieldsplit',
                                                                                                                    'pc_fieldsplit_type': 'schur',
                                                                                                                    'fieldsplit_0': {'ksp_type': 'default',
                                                                                                                                     'pc_type': 'jacobi',
                                                                                                                                     'ksp_rtol': 1.e-12,
                                                                                                                                     'ksp_atol': 1.e-12},
                                                                                                                    'fieldsplit_1': {'ksp_rtol': 1.e-10,
                                                                                                                                     'ksp_atol': 1.e-10}},
                                                                                                     'pc_python_type': 'firedrake.GTMGPC',
                                                                                                     'gt': gt_params_fully_matfree_matexpmg_assembledjacobi,
                                                                                                     'ksp_view': None,
                                                                                                     'ksp_monitor': None,
                                                                                                     'ksp_converged_reason': None}}


class DGLaplacian3D(AuxiliaryOperatorPC):
    def form(self, pc, u, v):
        W = u.function_space()
        n = FacetNormal(W.mesh())
        alpha = Constant(3.**5)
        gamma = Constant(4.**5)
        h = CellVolume(W.mesh())/FacetArea(W.mesh())
        h_avg = (h('+') + h('-'))/2

        a_dg = -(dot(grad(v), grad(u))*dx()
                 - dot(grad(v), (u)*n)*ds_v()
                 - dot(v*n, grad(u))*ds_v()
                 + gamma/h*dot(v, u)*ds_v()
                 - dot(grad(v), (u)*n)*ds_t()
                 - dot(v*n, grad(u))*ds_t()
                 + gamma/h*dot(v, u)*ds_t()
                 - dot(grad(v), (u)*n)*ds_b()
                 - dot(v*n, grad(u))*ds_b()
                 + gamma/h*dot(v, u)*ds_b()
                 - inner(jump(u, n), avg(grad(v)))*dS_v
                 - inner(avg(grad(u)), jump(v, n), )*dS_v
                 + alpha/h_avg * inner(jump(u, n), jump(v, n))*dS_v
                 - inner(jump(u, n), avg(grad(v)))*dS_h
                 - inner(avg(grad(u)), jump(v, n), )*dS_h
                 + alpha/h_avg * inner(jump(u, n), jump(v, n))*dS_h)

        bcs = []
        return (a_dg, bcs)


gtmg_fully_matfree_params_fs0_cg_jacobi_fs1_cg_jacobi = {'snes_type': 'ksponly',
                                                         'mat_type': 'matfree',
                                                         'ksp_type': 'preonly',
                                                         'pc_type': 'python',
                                                         'pc_python_type': 'firedrake.HybridizationPC',
                                                         'hybridization': {'ksp_type': 'cg',
                                                                           'pc_type': 'python',
                                                                           'mat_type': 'matfree',
                                                                           'ksp_rtol': 1.e-6,
                                                                           'ksp_atol': 1.e-6,
                                                                           'localsolve': {'ksp_type': 'preonly',
                                                                                          'mat_type': 'matfree',  # local-matfree!
                                                                                          'pc_type': 'fieldsplit',
                                                                                          'pc_fieldsplit_type': 'schur',
                                                                                          'fieldsplit_0': {'ksp_type': 'default',
                                                                                                           'pc_type': 'jacobi',
                                                                                                           'ksp_rtol': 1.e-12,
                                                                                                           'ksp_atol': 1.e-12,
                                                                                                           'pc_type': 'jacobi',
                                                                                                           'ksp_rtol': 1.e-10,
                                                                                                           'ksp_atol': 1.e-10}},
                                                                           'pc_python_type': 'firedrake.GTMGPC',
                                                                           'gt': gt_params_fully_matfree,
                                                                           'ksp_view': None,
                                                                           'ksp_monitor': None}}


gtmg_fully_matfree_params_fs0_cg_jacobi_fs1_cg_laplacian_jacobi_fgmres = {'snes_type': 'ksponly',
                                                                          'mat_type': 'matfree',
                                                                          'ksp_type': 'preonly',
                                                                          'pc_type': 'python',
                                                                          'pc_python_type': 'firedrake.HybridizationPC',
                                                                          'hybridization': {'ksp_type': 'fgmres',
                                                                                            'pc_type': 'python',
                                                                                            'mat_type': 'matfree',
                                                                                            'ksp_rtol': 1.e-6,
                                                                                            'ksp_atol': 1.e-6,
                                                                                            'localsolve': {'ksp_type': 'preonly',
                                                                                                           'mat_type': 'matfree',  # local-matfree!
                                                                                                           'pc_type': 'fieldsplit',
                                                                                                           'pc_fieldsplit_type': 'schur',
                                                                                                           'fieldsplit_0': {'ksp_type': 'default',
                                                                                                                            'pc_type': 'jacobi',
                                                                                                                            'ksp_rtol': 1.e-12,
                                                                                                                            'ksp_atol': 1.e-12},
                                                                                                           'fieldsplit_1': {'ksp_type': 'default',
                                                                                                                            'pc_type': 'python',
                                                                                                                            'pc_python_type': __name__ + '.DGLaplacian3D',
                                                                                                                            'aux_ksp_type': 'preonly',
                                                                                                                            'aux_pc_type': 'jacobi',
                                                                                                                            'ksp_rtol': 1.e-10,
                                                                                                                            'ksp_atol': 1.e-10}},
                                                                                            'pc_python_type': 'firedrake.GTMGPC',
                                                                                            'gt': gt_params_fully_matfree,
                                                                                            'ksp_view': None,
                                                                                            'ksp_monitor': None}}
