import time
from matplotlib import pyplot as plt 
from test import *
from maxrect import *

'''How does this vary on input size??'''

for x in range(1000):
	for y in range(1000):
		print "Grid %s by %s :" % (str(x), str(y))
		verbose_mode= "-v" in args[-1]
        clustering, density= 10.0, 65.0
        if len(args)>1:
            clutering, density = map(float, args[1:3])
        print 'Finding random grid....'
        grid = build_random_grid(x,y) if len(args)==3 else build_random_grid(x,y, clustering, density)
        print 'Found at %s' % (str(time.now()))
        print 'Translating into Bipartite Tables'
        new_grid= find_points(grid)
        nodes = find_corresponding_concave_points(new_grid)
        #draw_lines(new_grid)
        tables= build_table(nodes)
        print "Found %s concave points that can be connected to on another and assorted them into %s tables at %s" % (str(len(nodes)), str(len(tables)), str(time.now()))
        for count, table in enumerate(tables):
            table.matching_algo()
            print 'Found optimal matching for table # %s with %s nodes; sorted nodes into max set of min vertex cover' % (str(count), str(len(table)))
            if verbose_mode:
                print table
            print 'Adding lines...'
            new_grid, first_lines =add_lines(new_grid, table)
            print 'Added'
        print 'Done at %s' (str(time.now()))
