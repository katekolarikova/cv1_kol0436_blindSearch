from function_definitions.ackley_definition import AckleyFunction
from function_definitions.griewank_definition import GriewankFunction
from function_definitions.levy_definition import LevyFunction
from function_definitions.michalewicz_definition import MichalewiczFunction
from function_definitions.rastrigin_definition import RastriginFunction
from function_definitions.rosenbrock_definition import RosenbrockFunction
from function_definitions.schewel_definition import SchewelFunction
from function_definitions.sphere_definition import SphereFunction
from function_definitions.zakharov_definition import ZakharovFunction
from plot_print import Print3DPlot

# sphere
# rosenbrock
# ackley
# rastrigin
# schwefel
# griewank
# Levy
# Michalewicz
# Zakharov


if __name__=="__main__":
    Print3DPlot(AckleyFunction)