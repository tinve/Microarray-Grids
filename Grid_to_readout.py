__author__ = 'galina'
## Reads txt grid files. First column is x coordinate (in pixels), second

import numpy
import os

# image metadata
x0 = -9997.27
y0 = -21600.5
pix = 10

# desired reference point margin on the edge of the array
margin = 8

# directory with grid files
directory = "Grid"

# loads grid file from the path, generates and returns two arrays:
# readout_fast with physical fast coordinates
# readout_slow with physical slow coordinates
# each array has prepended number of readout points
# referencing is in the fast direction

def grid_readouts(path, x0=0, y0=0, pix=10, margin=8):

    grid = numpy.loadtxt(path, skiprows=1)  # txt file to list, skip header
    grid = numpy.array(grid).T.tolist()  # transpose to list of two lists (fast and slow)

    rows = int(grid[0].pop(0))  # cleave number of rows and columns from coordinate lists
    columns = int(grid[1].pop(0))

    grid = to_physical(grid, x0, y0, pix)  # convert pixel coordinates to physical coordinates


    # grid is rectangular, so fast and slow coordinates repeat. This bit removes redundant coordinates
    readout_fast = grid[0][0:columns]
    readout_slow = []
    for i in range(0, len(grid[1]), columns):
        readout_slow.append(grid[1][i])

    readout_fast = to_readout(readout_fast, margin, pix)  # adds reference points to fast coordinates

    # adds "header" - number of readout points in coordinate sequence
    readout_fast.insert(0, 2*columns + 1)
    readout_slow.insert(0, rows)

    readout_fast = rows * readout_fast

    return [readout_fast, readout_slow]

# takes list of fast and slow coordinates lists and converts into physical coordinates:
# scales each pixel coordinate by pixel size (in microns) and adds x or

def to_physical(grid, x0=0, y0=0, pix=1):
    grid[0] = [pix*x+x0 for x in grid[0]]
    grid[1] = [pix*y+y0 for y in grid[1]]
    return grid


# takes a list of coordinates and inserts intermediate points between each two elements.
# on edges adds reference points a margin distance away (in pixels)
def to_readout(x, margin = 8, pix = 1):
    result = [x[0] - margin*pix]
    for i in range(len(x)-1):
        result.append(x[i])
        result.append((x[i]+x[i+1])/2)
    result.append(x[-1])
    result.append(x[-1] + margin*pix)
    return result

readout_fast = []
readout_slow = []

files = os.listdir(directory)

# reads each grid file from the directory, generates readout fast and slow sequences and appends them together
for f in files:
#    print f
    readouts = grid_readouts(directory + '/' + f, x0, y0, pix, margin)
    readout_fast.append(readouts[0])
    readout_slow.append(readouts[1])

numpy.savetxt("readout_fast.txt", readout_fast, fmt = "%f", delimiter = "\n")
numpy.savetxt("readout_slow.txt", readout_slow, fmt = "%f", delimiter = "\n")
