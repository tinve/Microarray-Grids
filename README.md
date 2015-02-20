# Microarray-Grids
Grids processing script

**Grid_to_readout.py**
Single grid processing
I have a rectangular (but not regular grid). For example, a 3x4 grid like this one:

  o------o------o------o  
  |      |      |      |  
  o------o------o------o  
  |      |      |      |  
  o------o------o------o  
  
It has twelve points (called target points) and each of them has X (or fast) and Y (or slow) coordinate. Grid is rectangular, so coordinates repeat from row to row of from column to column, but it is not regular, so the spacing between the rows or columns can vary.

Grid is recorded in tab delimited txt file. First line contains grid type, second - number of rows and number of columns, followed by X and Y coordinates of each target point, from left to right and from bottom to top. The grid above can have a grid file like this (in general, all coordinates can be fractions):

Point Grid  
3 4  
11  3  
15  3  
20  3  
24  3  
11  9  
15  9  
20  9  
24  9  
11  14  
15  14  
20  14  
24  14  

I convert these pixel coordinates into physical coordinates (microns). Each coordinate needs to be multiplied by pixel size, offset x0 has to be added to all X (fast) coordinates and y0 - to all Y (slow) coordinates. For pixel size 10, x0 = 1000 and y = 2000, I'd get:

Point Grid  
3 4  
1110  2030  
1150  2030  
1200  2030  
1240  2030  
1110  2090  
1150  2090  
1200  2090  
1240  2090  
1110  2140  
1150  2140  
1200  2140  
1240  2140  

Now I need to add so called reference points in the fast direction, i.e. points in between each neighboring target points:

x o--x--o--x--o--x--o x  
  |     |     |     |  
x o--x--o--x--o--x--o x  
  |     |     |     |  
x o--x--o--x--o--x--o x  

Intermediate points are exactly in the middle, distance to edge reference points is given in pixels.

For this new grid I need to produce a list of Y (slow) coordinates with the number of distinct coordinates specified, and record it to text file:

3  
2030  
2090  
2140  

I also need array of nine X coordinates in physical units, prepended by the number of coordinates. It should look like this (target coordinates in bold font, margin is 5 pixels):

9  
1060  
**1110**  
1130  
**1150**  
1175  
**1200**  
1220  
**1240**  
1290  

And I need three duplicates of this array binded together and recorded to a single text file.

Multiple grid processing
Read grid files from a given directory, produce fast _ readout and slow _ readout for each of them and 



