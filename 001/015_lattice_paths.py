# -*- coding: utf-8 -*-
'''
Problem 15 - Lattice paths
Issue - #16
Description -
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

'''
0 0 0
0 0 0
0 0 0
r c r c r c r c r c
0 0
    0 1
        0 2
            1 2
                2 2
        1 1
            1 2
                2 2
            2 1
                2 2
    1 0
        1 1
            1 2
                2 2
            2 1
                2 2
        2 0
            2 1
                2 2
'''
#path_count = 0
max_grid = 20
'''
max_lattice = (max_grid, max_grid)

col_inc = lambda idx: (idx[0], idx[1] + 1) if idx[1] < max_grid else None
row_inc = lambda idx: (idx[0] + 1, idx[1]) if idx[0] < max_grid else None
'''
def main():
    paths = 1
    n = 2 * max_grid
    for k in range(1, max_grid + 1):
        paths *= ((n + 1) - k)/k
    print(paths)
'''
def traverse(node):
    print(node)
    global path_count
    row_lattice = row_inc(node)
    #print(row_lattice)
    if(row_lattice == max_lattice):
        path_count += 1
    elif(row_lattice is not None):
        traverse(row_lattice)
    col_lattice = col_inc(node)
    #print(col_lattice)
    if(col_lattice == max_lattice):
        path_count += 1
    elif(col_lattice is not None):
        traverse(col_lattice)
'''
if __name__ == '__main__':
    main()
    #print(path_count)
