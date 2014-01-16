MaxRect 
==============
Find minimum rectangles for a rectangular polygon.  Uses bipartite graph.
Jonathan Leslie: MIT License.  Distribute Freely
Jan, 2014
--------------

**Dependencies**: 
- Pyplot (but only in order to see it)

**Guidelines**

- Grid comes in the form of 1s and 0s
- Test.py will generate random grid of default size 30 by 30
- Can be run from command line: arg1 by arg2 grid with arg3 solidity and arg4 density & -v for verbose mode (e.g. python test.py 50 50 10 65 -v)
- Corresponding concave points are found then entered into bipartite graph, based on intersections as links.
- Then, the Bipartite Graph matching uses Hopcroft Karp (Augmenting Path) algorthm 
- Other concave points are drawn through to nearest edge and voila.

**Notes**
- Right now, draws edges on grid but does not return rectangles in a set of tuples as might be desirable


**Sample Input**

	./test.py 50 50 10 65 -v


**Sample Output**

Final display (Random Grid in Red; Rectangles Drawn in Blue): 

![ScreenShot](https://raw.github.com/jhiker/Maxrect.py/master/Screenshot.png)

         Random Grid:
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0]
[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
[1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Press enter to continue
Found 106 concave points that can be connected to on another and assorted them into 55 tables
Found optimal matching for table # 0 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 38 to 44 on 1.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 1 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 30 to 35 on 48.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 2 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 30 to 44 on 48.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 3 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 32 to 34 on 33.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 4 with 2 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 8 to 10 on 45.  Links: set([1 Line: 35 to 46 on 9]). Part of vertex cover Matched: True

 column ver: 1 Line: 35 to 46 on 9.  Links: set([0 Line: 8 to 10 on 45]). Part of Max Set Matched: True

Found optimal matching for table # 5 with 2 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 27 to 30 on 39.  Links: set([1 Line: 36 to 44 on 28]). Part of vertex cover Matched: True

 column ver: 1 Line: 36 to 44 on 28.  Links: set([0 Line: 27 to 30 on 39]). Part of Max Set Matched: True

Found optimal matching for table # 6 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 13 to 15 on 34.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 7 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 32 to 34 on 15.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 8 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 23 to 25 on 34.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 9 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 43 to 45 on 40.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 10 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 36 to 39 on 30.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 11 with 11 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 15 to 21 on 36.  Links: set([1 Line: 31 to 39 on 19]). Part of Max Set Matched: True

0 Line: 18 to 20 on 38.  Links: set([1 Line: 31 to 39 on 19]). Part of Max Set Matched: False

0 Line: 17 to 19 on 28.  Links: set([1 Line: 26 to 36 on 18]). Part of Max Set Matched: True

0 Line: 16 to 19 on 31.  Links: set([1 Line: 28 to 34 on 17, 1 Line: 26 to 36 on 18]). Part of Max Set Matched: True

0 Line: 15 to 27 on 32.  Links: set([1 Line: 31 to 39 on 19, 1 Line: 31 to 34 on 25, 1 Line: 28 to 34 on 17, 1 Line: 26 to 36 on 18]). Part of vertex cover Matched: True

0 Line: 16 to 19 on 29.  Links: set([1 Line: 28 to 34 on 17, 1 Line: 26 to 36 on 18]). Part of Max Set Matched: False

0 Line: 17 to 21 on 34.  Links: set([1 Line: 31 to 39 on 19, 1 Line: 26 to 36 on 18]). Part of Max Set Matched: False

 column ver: 1 Line: 26 to 36 on 18.  Links: set([0 Line: 15 to 27 on 32, 0 Line: 16 to 19 on 31, 0 Line: 17 to 19 on 28, 0 Line: 17 to 21 on 34, 0 Line: 16 to 19 on 29]). Part of vertex cover Matched: True

1 Line: 31 to 39 on 19.  Links: set([0 Line: 18 to 20 on 38, 0 Line: 15 to 27 on 32, 0 Line: 17 to 21 on 34, 0 Line: 15 to 21 on 36]). Part of vertex cover Matched: True

1 Line: 28 to 34 on 17.  Links: set([0 Line: 15 to 27 on 32, 0 Line: 16 to 19 on 29, 0 Line: 16 to 19 on 31]). Part of vertex cover Matched: True

1 Line: 31 to 34 on 25.  Links: set([0 Line: 15 to 27 on 32]). Part of Max Set Matched: True

Found optimal matching for table # 12 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 36 to 39 on 32.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 13 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 7 to 13 on 40.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 14 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 9 to 16 on 46.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 15 with 3 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 15 to 21 on 22.  Links: set([1 Line: 17 to 24 on 18, 1 Line: 21 to 23 on 19]). Part of vertex cover Matched: True

 column ver: 1 Line: 17 to 24 on 18.  Links: set([0 Line: 15 to 21 on 22]). Part of Max Set Matched: True

1 Line: 21 to 23 on 19.  Links: set([0 Line: 15 to 21 on 22]). Part of Max Set Matched: False

Found optimal matching for table # 16 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 42 to 44 on 16.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 17 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 38 to 44 on 18.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 18 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 46 to 48 on 30.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 19 with 2 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 22 to 25 on 4.  Links: set([1 Line: 3 to 7 on 23]). Part of Max Set Matched: True

 column ver: 1 Line: 3 to 7 on 23.  Links: set([0 Line: 22 to 25 on 4]). Part of vertex cover Matched: True

Found optimal matching for table # 20 with 4 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 32 to 48 on 44.  Links: set([1 Line: 42 to 45 on 41, 1 Line: 42 to 45 on 43, 1 Line: 42 to 47 on 45]). Part of vertex cover Matched: True

 column ver: 1 Line: 42 to 47 on 45.  Links: set([0 Line: 32 to 48 on 44]). Part of Max Set Matched: True

1 Line: 42 to 45 on 41.  Links: set([0 Line: 32 to 48 on 44]). Part of Max Set Matched: False

1 Line: 42 to 45 on 43.  Links: set([0 Line: 32 to 48 on 44]). Part of Max Set Matched: False

Found optimal matching for table # 21 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 17 to 20 on 43.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 22 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 10 to 13 on 2.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 23 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 9 to 12 on 1.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 24 with 2 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 36 to 44 on 29.  Links: set([1 Line: 28 to 40 on 43]). Part of Max Set Matched: True

 column ver: 1 Line: 28 to 40 on 43.  Links: set([0 Line: 36 to 44 on 29]). Part of vertex cover Matched: True

Found optimal matching for table # 25 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 2 to 4 on 13.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 26 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 32 to 40 on 47.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 27 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 32 to 38 on 41.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 28 with 3 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 42 to 45 on 7.  Links: set([1 Line: 4 to 11 on 44]). Part of Max Set Matched: False

0 Line: 42 to 45 on 5.  Links: set([1 Line: 4 to 11 on 44]). Part of Max Set Matched: True

 column ver: 1 Line: 4 to 11 on 44.  Links: set([0 Line: 42 to 45 on 5, 0 Line: 42 to 45 on 7]). Part of vertex cover Matched: True

Found optimal matching for table # 29 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 36 to 41 on 23.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 30 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 40 to 44 on 13.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 31 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 32 to 40 on 45.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 32 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 29 to 33 on 9.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 33 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 20 to 25 on 7.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 34 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 16 to 21 on 1.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 35 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 29 to 35 on 8.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 36 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 38 to 40 on 16.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 37 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 30 to 32 on 10.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 38 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 30 to 35 on 46.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 39 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 13 to 15 on 46.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 40 with 9 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 16 to 21 on 3.  Links: set([1 Line: 1 to 11 on 18, 1 Line: 1 to 4 on 20]). Part of vertex cover Matched: True

0 Line: 13 to 15 on 8.  Links: set([1 Line: 5 to 11 on 14]). Part of Max Set Matched: True

0 Line: 14 to 16 on 11.  Links: set([1 Line: 8 to 13 on 15]). Part of Max Set Matched: True

0 Line: 13 to 24 on 10.  Links: set([1 Line: 5 to 11 on 14, 1 Line: 8 to 13 on 15, 1 Line: 1 to 11 on 18]). Part of vertex cover Matched: True

0 Line: 11 to 15 on 6.  Links: set([1 Line: 5 to 11 on 14]). Part of Max Set Matched: False

 column ver: 1 Line: 1 to 11 on 18.  Links: set([0 Line: 16 to 21 on 3, 0 Line: 13 to 24 on 10]). Part of vertex cover Matched: True

1 Line: 1 to 4 on 20.  Links: set([0 Line: 16 to 21 on 3]). Part of Max Set Matched: True

1 Line: 5 to 11 on 14.  Links: set([0 Line: 13 to 24 on 10, 0 Line: 11 to 15 on 6, 0 Line: 13 to 15 on 8]). Part of vertex cover Matched: True

1 Line: 8 to 13 on 15.  Links: set([0 Line: 13 to 24 on 10, 0 Line: 14 to 16 on 11]). Part of vertex cover Matched: True

Found optimal matching for table # 41 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 43 to 45 on 42.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 42 with 13 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 22 to 38 on 18.  Links: set([1 Line: 13 to 24 on 29, 1 Line: 12 to 19 on 24, 1 Line: 16 to 19 on 25, 1 Line: 12 to 23 on 34, 1 Line: 14 to 19 on 27, 1 Line: 15 to 23 on 36]). Part of vertex cover Matched: True

0 Line: 29 to 36 on 15.  Links: set([1 Line: 12 to 23 on 34]). Part of Max Set Matched: True

0 Line: 18 to 27 on 14.  Links: set([1 Line: 12 to 19 on 24]). Part of Max Set Matched: True

0 Line: 26 to 41 on 22.  Links: set([1 Line: 13 to 24 on 29, 1 Line: 15 to 23 on 36, 1 Line: 12 to 23 on 34]). Part of Max Set Matched: True

0 Line: 22 to 44 on 17.  Links: set([1 Line: 13 to 24 on 29, 1 Line: 12 to 19 on 24, 1 Line: 16 to 19 on 25, 1 Line: 12 to 23 on 34, 1 Line: 14 to 19 on 27, 1 Line: 15 to 23 on 36, 1 Line: 15 to 18 on 40]). Part of vertex cover Matched: True

0 Line: 33 to 36 on 13.  Links: set([1 Line: 12 to 23 on 34]). Part of Max Set Matched: False

 column ver: 1 Line: 13 to 24 on 29.  Links: set([0 Line: 22 to 38 on 18, 0 Line: 22 to 44 on 17, 0 Line: 26 to 41 on 22]). Part of Max Set Matched: True

1 Line: 15 to 18 on 40.  Links: set([0 Line: 22 to 44 on 17]). Part of Max Set Matched: True

1 Line: 12 to 19 on 24.  Links: set([0 Line: 22 to 38 on 18, 0 Line: 18 to 27 on 14, 0 Line: 22 to 44 on 17]). Part of vertex cover Matched: True

1 Line: 15 to 23 on 36.  Links: set([0 Line: 22 to 38 on 18, 0 Line: 22 to 44 on 17, 0 Line: 26 to 41 on 22]). Part of vertex cover Matched: True

1 Line: 16 to 19 on 25.  Links: set([0 Line: 22 to 38 on 18, 0 Line: 22 to 44 on 17]). Part of Max Set Matched: False

1 Line: 12 to 23 on 34.  Links: set([0 Line: 29 to 36 on 15, 0 Line: 26 to 41 on 22, 0 Line: 33 to 36 on 13, 0 Line: 22 to 38 on 18, 0 Line: 22 to 44 on 17]). Part of vertex cover Matched: True

1 Line: 14 to 19 on 27.  Links: set([0 Line: 22 to 38 on 18, 0 Line: 22 to 44 on 17]). Part of Max Set Matched: False

Found optimal matching for table # 43 with 3 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 23 to 35 on 3.  Links: set([1 Line: 2 to 4 on 29, 1 Line: 1 to 4 on 25]). Part of vertex cover Matched: True

 column ver: 1 Line: 2 to 4 on 29.  Links: set([0 Line: 23 to 35 on 3]). Part of Max Set Matched: True

1 Line: 1 to 4 on 25.  Links: set([0 Line: 23 to 35 on 3]). Part of Max Set Matched: False

Found optimal matching for table # 44 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 29 to 32 on 1.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 45 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 40 to 43 on 15.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 46 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 7 to 17 on 47.  Links: set([]). Part of Max Set Matched: False

Found optimal matching for table # 47 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 8 to 24 on 48.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 48 with 4 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 3 to 11 on 16.  Links: set([1 Line: 12 to 24 on 7, 1 Line: 12 to 17 on 10]). Part of vertex cover Matched: True

0 Line: 5 to 9 on 23.  Links: set([1 Line: 12 to 24 on 7]). Part of Max Set Matched: True

 column ver: 1 Line: 12 to 17 on 10.  Links: set([0 Line: 3 to 11 on 16]). Part of Max Set Matched: True

1 Line: 12 to 24 on 7.  Links: set([0 Line: 3 to 11 on 16, 0 Line: 5 to 9 on 23]). Part of vertex cover Matched: True

Found optimal matching for table # 49 with 2 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 29 to 44 on 4.  Links: set([1 Line: 3 to 8 on 35]). Part of Max Set Matched: True

 column ver: 1 Line: 3 to 8 on 35.  Links: set([0 Line: 29 to 44 on 4]). Part of vertex cover Matched: True

Found optimal matching for table # 50 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 26 to 28 on 43.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 51 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 18 to 26 on 46.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 52 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 36 to 42 on 23.  Links: set([]). Part of Max Set Matched: False

 column ver:
Found optimal matching for table # 53 with 5 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor: 0 Line: 3 to 9 on 29.  Links: set([1 Line: 27 to 45 on 6, 1 Line: 27 to 45 on 8]). Part of vertex cover Matched: True

0 Line: 1 to 9 on 35.  Links: set([1 Line: 27 to 45 on 6, 1 Line: 29 to 44 on 3, 1 Line: 27 to 45 on 8]). Part of vertex cover Matched: True

 column ver: 1 Line: 29 to 44 on 3.  Links: set([0 Line: 1 to 9 on 35]). Part of Max Set Matched: True

1 Line: 27 to 45 on 8.  Links: set([0 Line: 3 to 9 on 29, 0 Line: 1 to 9 on 35]). Part of Max Set Matched: False

1 Line: 27 to 45 on 6.  Links: set([0 Line: 3 to 9 on 29, 0 Line: 1 to 9 on 35]). Part of Max Set Matched: True

Found optimal matching for table # 54 with 1 nodes; sorted nodes into max set of min vertex cover
Table:
 column hor:
 column ver: 1 Line: 35 to 47 on 1.  Links: set([]). Part of Max Set Matched: False

Found optimal cover in 137 rectangles
[4, 6, 2, 2, 2, 2, 3, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 4, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 4, 0, 7, 4, 6, 2, 2, 2, 3]
[0, 2, 1, 1, 1, 1, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 4, 0, 4, 0, 2, 2, 2, 2, 3]
[3, 2, 1, 1, 1, 1, 2, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 4, 0, 2, 2, 2, 1, 1, 1, 1, 2, 0, 2, 2, 2, 2, 6, 0, 6, 2, 2, 1, 2, 2, 0]
[2, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 2, 1, 2, 5, 4]
[2, 2, 1, 2, 0, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 3, 0, 3, 6, 0, 4, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 0]
[2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 0, 2, 1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 3]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 5, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 0, 3, 3, 0, 3, 2, 2, 2, 2, 6, 0, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 1, 2, 1, 2, 1, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 0, 3, 2, 2, 2, 1, 2, 0, 2, 1, 1, 1, 1, 1, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 0, 2, 1, 2, 5, 4, 2, 5, 2, 2, 0, 2, 1, 2, 1, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 2, 0, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 0, 2, 2, 2, 2, 2, 5, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, 1, 2, 2, 1, 5, 4, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0, 0, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]
[3, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 1, 2, 0, 2, 1, 2, 0, 0, 4, 0, 4, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]
[0, 2, 1, 2, 1, 2, 2, 1, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 6, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2]
[0, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 0, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 0, 0, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]
[3, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 0, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 0, 2, 1, 1, 1, 2, 0, 4, 0, 0, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 5, 2, 2, 0, 0, 3, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 5, 6, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2]
[2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 3, 0, 0, 0, 2, 1, 1, 2, 0, 0, 4, 0, 0, 3, 2, 2, 4, 7, 0, 4, 0, 4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 2, 2, 3]
[3, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 2, 0, 7, 4, 6, 0, 0, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3, 0]
[0, 4, 0, 2, 1, 2, 2, 1, 2, 2, 0, 6, 2, 3, 0, 3, 2, 2, 2, 2, 2, 2, 2, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 5, 5, 3, 0, 0, 0, 0, 0]
[4, 6, 6, 5, 2, 2, 2, 2, 2, 6, 4, 5, 1, 2, 0, 0, 0, 2, 2, 2, 0, 2, 2, 0, 0, 0, 7, 4, 4, 4, 6, 5, 4, 7, 0, 3, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 4, 0]
[0, 0, 3, 6, 0, 0, 4, 0, 4, 0, 0, 2, 2, 2, 2, 0, 4, 0, 6, 6, 4, 5, 2, 2, 4, 0, 4, 0, 0, 0, 3, 3, 0, 4, 0, 3, 2, 2, 2, 0, 0, 0, 6, 3, 0, 7, 4, 4, 0, 0]
[0, 0, 0, 7, 4, 7, 0, 3, 5, 3, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 2, 2, 2, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 4, 7, 0, 0, 4, 0]
[4, 2, 3, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 3, 2, 2, 2, 3, 0, 6, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 7, 6, 7]
[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 1, 1, 2, 2, 2, 6, 0, 2, 0, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 4, 0, 4]
[0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 2, 2, 4, 5, 1, 1, 2, 2, 1, 5, 4, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 4]
[3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 2, 2, 0, 2, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 2, 1, 2, 0, 3, 6, 7]
[2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 5, 4, 2, 6, 4, 6, 2, 2, 2, 2, 0, 4, 0, 0, 2, 3, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 0]
[2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 2, 0, 0, 3, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 2, 2, 1, 2, 2, 0, 0, 0, 0, 0]
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 2, 3, 0, 2]
[3, 2, 0, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 2, 2, 2, 2, 2, 2, 3, 0, 3, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 6, 4, 2, 2, 2, 2]
[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 5, 1, 2, 2, 0, 4, 0, 0, 0, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 2, 2, 1, 2]
[0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 6, 2, 2, 5, 2, 5, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2]
[0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 5, 4, 7, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2]
[0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 4, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2]
[3, 2, 2, 1, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 1, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 0, 2, 2, 1, 2]
[2, 2, 2, 1, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 4, 0, 0, 0, 3, 2, 3, 0, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2]
[2, 2, 2, 2, 3, 0, 3, 6, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2]
[3, 2, 3, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 1, 1, 1, 1, 2, 2, 0, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2]
[0, 4, 0, 0, 4, 0, 3, 6, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 0, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2]
[3, 5, 3, 0, 4, 0, 2, 2, 0, 0, 3, 2, 2, 2, 2, 2, 0, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2]
[2, 1, 2, 0, 4, 0, 2, 2, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 3, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, 2, 0, 2, 1, 2]
[2, 1, 2, 0, 4, 0, 3, 6, 4, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
[3, 2, 5, 2, 2, 2, 0, 0, 0, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 5, 2]
[0, 0, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 4, 0, 6, 3]
[3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 4, 0, 4, 0]
[2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 4, 5, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 5, 3]
[3, 2, 2, 2, 2, 2, 3, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 3, 3, 0, 4, 0, 3, 3, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
