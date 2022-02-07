import matplotlib.pyplot as plt
import numpy as np
from AntColony import runAcoTsp

def main():

    # Number of cities
    #population_size = int(input("Please enter number of cities:\n"))
    population_size = 100

    # # Create n*n matrix and enter matrix or generate random numbers
    intermediateMatrix = np.random.randint(0, 100, size=(population_size, population_size))
    CityDistMatrix = np.tril(intermediateMatrix) + np.tril(intermediateMatrix, -1).T
    for i in range(0, population_size):
        CityDistMatrix[i][i] = 0
    # print(f'Distance Matrix: {CityDistMatrix}')
    space = CityDistMatrix

    #iterations = int(input("Please enter number of iterations:\n"))
    iterations = 50

    #colony = int(input("Please enter number of ants:\n"))
    colony = 25

    # alpha = int(input("Please enter alpha value:\n"))
    alpha = 1
    # beta = int(input("Please enter beta value:\n"))
    beta = 1
    del_tau = 1.5

    #rho = float(input("Please enter evaporation rate:\n"))
    rho = 0.5 #evaporation rate

    min_path, min_distance, progress, iter = runAcoTsp(space, iterations, colony, alpha, beta, del_tau, rho)

    plt.plot(iter, progress)
    plt.ylabel('Distance')
    plt.xlabel('Iteration')
    plt.show()

if __name__ == '__main__':
    main()

