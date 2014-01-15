MaxRect 
==============
Find minimum rectangles for a rectangular polygon.  Uses bipartite graph.
Jonathan Leslie: MIT License.  Distribute Freely
Jan, 2014
--------------

**Guidelines**
-Dependencies: Pyplot (in order to see it)

**Guidelines**

- Grid comes in the form of 1s and 0s
- Test.py will generate random grid of default size 30 by 30
- Can be run from command line: arg1 by arg2 grid with arg3 solidity and arg4 density & -v for verbose mode (e.g. python test.py 50 50 10 65 -v)
- Corresponding concave points are found then entered into bipartite graph, based on intersections as links.
- Then, the Bipartite Graph matching uses Hopcroft Karp (Augmenting Path) algorthm 
- Other concave points are drawn through to nearest edge and voila.

**Notes**
- Right now, draws edges on grid but does not return rectangles in a set of tuples as might be desirable


	