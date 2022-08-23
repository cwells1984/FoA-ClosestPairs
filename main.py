import csv
import inputgenerator
import math
import time

# Constants
INPUT_FILE = 'input.csv'
M = 5

# this reads the input csv and creates a list of points with coordinate pairs as a dictionary
# 'name' = point name
# 'x' and 'y' = point x and y coordinates
def readInput(inputFile):
    with open(inputFile, 'r') as csvfile:
        pairs = list(csv.DictReader(csvfile))
    return pairs


# calculates distances between 2 pairs of x and y coordinates
# returns the distance as a float
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


# returns a list of the m closest coordinate pairs in a given set of input points
# P = a list of pair dictionaries assembled by readInput() above
# m = integer of how many distances to return
def closest_pairs(pairs, m):
    distancePairs = []

    # first calculate the distances between each pair of points
    for i in range(len(pairs)):
        point1 = pairs[i]

        for j in range(i+1, len(pairs)):
            point2 = pairs[j]
            d = distance(int(point1['x']), int(point1['y']), int(point2['x']), int(point2['y']))
            pairName = point1['name'] + "-" + point2['name']
            distancePairs.append({'name':pairName, 'distance':d})

    # now do a simple bubble sort to sort the distances from shortest to largest
    for i in range(len(distancePairs)):
        for j in range(len(distancePairs) - i - 1):
            if float(distancePairs[j]['distance']) > float(distancePairs[j+1]['distance']):
                temp = distancePairs[j]
                distancePairs[j] = distancePairs[j+1]
                distancePairs[j+1] = temp

    # finally return the first m entries in the array - the m closest point pairs
    return distancePairs[0:m]


def run_closest_points(numPoints):
    # generate input...
    inputgenerator.generate_input(INPUT_FILE, numPoints)

    # set the timer and execute...
    startTime = time.time()
    pairs = readInput(INPUT_FILE)
    distancePairs = closest_pairs(pairs, M)
    endTime = time.time()

    # ... and print output
    print ("Input Size: %s points" % len(pairs))
    print (str(M) + " Closest distances (calculated in %s seconds)" % (endTime - startTime))
    for distancePair in distancePairs:
        print "Distance " + distancePair['name'] + ": " + str(distancePair['distance'])
    print ""


run_closest_points(10)
run_closest_points(20)
run_closest_points(30)
run_closest_points(40)
run_closest_points(50)