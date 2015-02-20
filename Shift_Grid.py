__author__ = 'galina'
## Reads txt grid files. First column is x coordinate (in pixels), second

import numpy
import os

# shifts in pixels
x_shift = 10.5
y_shift = -1.0

# directory with grid files
directory = "test"


def grid_shift(path, x_shift = 0, y_shift = 0):

# reads txt grid file, extracts fast and slow coordinates, shifs them by x_shift and y_shift respectively,
# overwrites the file with the shifted coordinates

    grid = numpy.loadtxt(path, skiprows=1)  # txt file to list, skip header
    grid = numpy.array(grid).T.tolist()  # transpose to list of two lists (fast and slow)

    rows = int(grid[0].pop(0))  # cleave number of rows and columns from coordinate lists
    columns = int(grid[1].pop(0))

#    grid[0] = shift(grid[0], x_shift)  # shifts fast and slow coordinates independently
#    grid[1] = shift(grid[1], y_shift)

    path_to_write =

    f = open(path_to_write, "w")
    f.write("Point tab Grid\n")
    f.write("%i tab %i\n" % rows % columns)

    for i in range(len(grid[0])):
        f.write("%f tab %f\n" % grid[0][i] % grid[1][i])

    f.close()

files = os.listdir(directory)
files.sort()

# reads each grid file from the directory, generates readout fast and slow sequences and writes to new files
for f_name in files:
    grid_shift(os.path.join(directory, f_name), x_shift, y_shift)

