#!/bin/sh

# Same as 4c but with assembled jacobi as smoother
export ORDERS=(0 1 2 3 4 5)
export LEVELS=2
export SCALING=(2)
export DEFORM=(0)
export TRAFO='none' # 'affine'
export ATQD=(0 0)
export CELLSPD=(4)
export QUADS=true
export FLAME=true
export BASEP='gtmg_global_matfree_params_matexpmg_assembledjacobi_fgmres'
export PERFORMP='gtmg_fully_matfree_params_matexpmg_fgmres_assembledjacobi'
export SOLTYPE='exponential'
export PROJECTEXACTSOL="" #--projectexactsol
export CASE='/case4e/'