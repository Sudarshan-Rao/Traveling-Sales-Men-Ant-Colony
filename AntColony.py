import numpy as np

def runAcoTsp(space, iterations = 80, colony = 50, alpha = 1.0, beta = 1.0, del_tau = 1.0, rho = 0.5):
    print("Ant colony started")
    inv_distances = inverseDistances(space)
    inv_distances = inv_distances ** beta
    pheromones = np.zeros((space.shape[0], space.shape[0]))

    min_distance = None
    min_path = None
    progress = []
    iter = []

    for i in range(iterations):
        positions = initializeAnts(space, colony)
        paths = moveAnts(space, positions, inv_distances, pheromones, alpha, beta, del_tau)
        pheromones *= (1 - rho)

        for path in paths:
            distance = 0
            distance = calcDistance(path , space)

            if not min_distance or distance < min_distance:
                min_distance = distance
                min_path = path

        progress.append(min_distance)
        iter.append(i)
    return (min_path, min_distance, progress, iter)

def inverseDistances(space):
    with np.errstate(all = 'ignore'):
        inv_distances = 1. / space
    inv_distances[inv_distances == np.inf] = 0
    return inv_distances

def initializeAnts(space, colony):
    return np.random.randint(space.shape[0], size = colony)

def moveAnts(space, positions, inv_distances, pheromones, alpha, beta, del_tau):
    paths = np.zeros((space.shape[0], positions.shape[0]), dtype = int) - 1

    paths[0] = positions

    for node in range(1, space.shape[0]):

        for ant in range(positions.shape[0]):

            next_location_probability = (inv_distances[positions[ant]] ** alpha + pheromones[positions[ant]] ** beta /
                                            inv_distances[positions[ant]].sum() ** alpha + pheromones[positions[ant]].sum() ** beta)


            next_position = np.argwhere(next_location_probability == np.amax(next_location_probability))[0][0]

            while next_position in paths[:, ant]:

                next_location_probability[next_position] = 0.0

                next_position = np.argwhere(next_location_probability == np.amax(next_location_probability))[0][0]

            paths[node, ant] = next_position

            pheromones[node, next_position] = pheromones[node, next_position] + del_tau

    return np.swapaxes(paths, 0, 1)

def calcDistance(instanceList, distanceList):
    pathDistance = 0
    for i in range(0, len(instanceList)):
        fromCity = instanceList[i]
        if i + 1 < len(instanceList):
            toCity = instanceList[i + 1]
        else:
            toCity = instanceList[0]

        pathDistance += distanceList[fromCity][toCity]

    return pathDistance