__author__ = 'galina'
## Reads txt grid files. First column is x coordinate (in pixels), second

import numpy
import os
import shutil

# shifts in pixels
x_shift = 1.5
y_shift = -10.0

# directory with grid files
directory = "test"
new_directory = "shifted"


def grid_shift(path, directory_path, x_shift = 0, y_shift = 0):

# reads txt grid file, extracts fast and slow coordinates, shifs them by x_shift and y_shift respectively,
# overwrites the file with the shifted coordinates

    grid = numpy.loadtxt(path, skiprows=1)  # txt file to list, skip header
    grid = numpy.array(grid).T.tolist()  # transpose to list of two lists (fast and slow)

    rows = int(grid[0].pop(0))  # cleave number of rows and columns from coordinate lists
    columns = int(grid[1].pop(0))

    grid[0] = [x + x_shift for x in grid[0]]  # add shift to each coordinate
    grid[1] = [y + y_shift for y in grid[1]]

    path_to_write = os.path.join(directory_path, os.path.basename(path)) #write to new folder under old name

    f = open(path_to_write, "w")
    f.write("Point\tGrid\n")  # header
    f.write("%d\t%d\n" % (rows, columns))  # rows and columns

    for i in range(len(grid[0])):  # shifted coordinates
        f.write("%.4f\t%.4f\n" % (grid[0][i], grid[1][i]))

    f.close()

files = os.listdir(directory)
files.sort()

# make output directory inside grid directory. If it already exists, delete all files inside
directory_to_write = os.path.join(directory, new_directory)

if os.path.exists(directory_to_write):
    shutil.rmtree(directory_to_write)

os.makedirs(directory_to_write)


# reads each grid file from the directory, generates readout fast and slow sequences and writes to new files
for f_name in files:
    grid_shift(os.path.join(directory, f_name), directory_to_write, x_shift, y_shift)

