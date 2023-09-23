import numpy as np
import matplotlib.pyplot as plt

from blind_search import BlindSearch
from function_definitions.ackley_definition import AckleyFunction
def Print3DPlot(func):
    r_min, r_max = -32.768, 32.768 # usuall range for Ackley function
    x = np.linspace(r_min, r_max, 15)
    y = np.linspace(r_min, r_max, 15)
    X, Y = np.meshgrid(x, y) #create X, Y grid
    # Z = np.zeros_like(X)
    Z = func(X, Y) #compute Z value for each point of grid
    #
    # for i in range(len(x)):
    #     for j in range(len(y)):
    #         Z[i, j] = Rastrigin([X[i, j], Y[i, j]])

    # Vytvoření 3D grafu
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='hot', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Ackley(X, Y)')

    # Přidání barevného průběhu a zobrazení legendy
    fig.colorbar(surf)

    #
    xy_points = list(zip(X.ravel(), Y.ravel()))
    pointsHistory = BlindSearch(func, 1000, r_min, r_max, r_min, r_max)
    for point in pointsHistory:
        ax.scatter(point[0], point[1], point[2], c='blue', marker='o')
    # Zobrazení grafu
    plt.show()