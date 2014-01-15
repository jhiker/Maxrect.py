#! /usr/bin/env python

#Author Jonathan Leslie: Test for Maxrect

'''Automatically generate a grid with command line: enter width and length as first two args, then can enter 
consistency and density'''
from random import random
from sys import argv as args
from matplotlib import pyplot as plt 



def build_random_grid(x, y, cal=10, dens=65):
    '''x= row, y = column, cal= clustering'''
    grid=[]
    for i in range(x): grid.append(list([0]*y))
    i=0
    for loop_ in (-1,1):
        midpoint=(x/2)*loop_
        while i != (midpoint):
            for j in range(y):
                calibrate=grid[i][j-1]+ grid[i-1][j]-1.5+.5*(grid[i][j-2]+grid[i-2][j])
                grid[i][j]=int((random()+calibrate*(cal/50))>(1-dens/100))
            i+=loop_

    return grid

test_1= [

[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
,
[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
,
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
,
[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1]
,
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
,
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
,
[1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
,
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
,
[1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
,
[1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
,
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0]
,
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
,
[1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0]
,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0]
,
[0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
,
[1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0]
,
[0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
,
[0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0]
,
[0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0]
,
[0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
,
]


if __name__=="__main__":
    from maxrect import *


    if len(args)>1:
        verbose_mode= "-v" in args[-1]
        if verbose_mode: args.pop()
        x,y = map(int, args[1:3])
        clustering, density= 10.0, 65.0
        clutering, density = map(float, args[3:5]) if len(args)>3 else 10.0, 65.0

        grid = build_random_grid(x,y) if len(args)==3 else build_random_grid(x,y, clustering, density)
        
        print 'Random Grid:'
        for g in reversed(grid):
            print g
        raw_input('Press enter to continue')
        new_grid= find_points(grid)
        nodes = find_corresponding_concave_points(new_grid)
        draw_lines(new_grid)
        tables= build_table(nodes)
        print "Found %s concave points that can be connected to on another and assorted them into %s tables" % (str(len(nodes)), str(len(tables)))
        for count, table in enumerate(tables):
            table.matching_algo()
            if verbose_mode:
                print 'Found optimal matching for table # %s with %s nodes; sorted nodes into max set of min vertex cover' % (str(count), str(len(table)))
                print table
            new_grid, first_lines =add_lines(new_grid, table)
        #draw_nodes(nodes)
        '''Uncomment line to see min set nodes drawn in green'''

    else:
        build_random_grid(10, 10)
        new_grid=find_points(grid)
        nodes = find_corresponding_concave_points(new_grid)
        draw_lines(new_grid)
        tables= build_table(nodes)
        for table in (tables):
            table.matching_algo() 
            new_grid, first_lines =add_lines(new_grid, table)
    final_grid, second_lines= draw_new_lines(new_grid)
    print "Found optimal cover in %s rectangles " % ( str(first_lines+second_lines))
    for row in reversed(final_grid):
        print row
    plt.show()

            
            



