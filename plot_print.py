import numpy as np
import matplotlib.pyplot as plt

from blind_search import BlindSearch

# this function print 3D plot of given function, and add points found by blind search to it
def Print3DPlot(func):
    r_min, r_max = -32.768, 32.768 # range of values for x and y
    x = np.linspace(r_min, r_max, 1500) # return array of evenly spaced values
    y = np.linspace(r_min, r_max, 1500)
    X, Y = np.meshgrid(x, y) #create X, Y grid from x, y arrays
    Z = func(X, Y) #compute Z value for each point of grid (func represents given type of plot)

    # Create a 3D plot
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='hot', alpha=0.5) # create a plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # add color bar to plot
    fig.colorbar(surf)

    # find by blind search
    pointsHistory = BlindSearch(func, 10000, r_min, r_max, r_min, r_max) # points found by blind search through time
    for point in pointsHistory:
        ax.scatter(point[0], point[1], point[2], c='blue', marker='o') # plot points

    # display plot
    plt.show()