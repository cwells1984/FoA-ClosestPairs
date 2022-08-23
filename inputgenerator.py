# this utility creates a list of randomly-placed coordinate points named numerically and outputs the list to
# input.csv
import random

MIN_X = 0
MAX_X = 100
MIN_Y = 0
MAX_Y = 100


def generate_input(file, numPoints):
    with open(file, 'w') as csvfile:
        csvfile.write("name,x,y\n")
        for i in range(1,numPoints+1):
            name = str(i)
            x = str(random.randint(MIN_X, MAX_X))
            y = str(random.randint(MIN_Y, MAX_Y))
            csvfile.write(name + "," + x + "," + y + "\n")
