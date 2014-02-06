#! /usr/bin/env python

#MAXRECT Author Jonathan Leslie, MIT License

from Bipartite import *
from matplotlib import pyplot as plt 


'''Maxrect: Determines minimum number of rectangles composing random rectangular polygon input in the form of a 2D grid made of 1s and 0s
Will draw rectangles  using pyplot'''

def find_points(grid):
    '''Transforms 1s on grid into range of integers representing types of points according to their proximal points 
    If concave (has at least two 1s for adjacent with a corresponding 0 diagnonal: >= 5
    Convex corners are 3; 4 is a bridge or edge on either side.
    Combine the above to get concave that are also convex etc.
    Edge or (one adjacent 0)  = 2 '''
    len_x, len_y, new_grid= len(grid), len(grid[0]), []
    for i in range(len_x): new_grid.append([0]*len_y)
    for x in range(len_x):
        for y in range(len_y):
            if grid[x][y]:
                spaces =   [grid[x+a*((x+a)<len_x)][y+b*((y+b)<len_y)]* (0<=(x+a)<len_x) * (0<= (y+b)<len_y )\
                            for a in range(-1,2) for b in range(-1,2)]
                #Spaces=array of all the proximal points and the point itself given nested comprehension above
                concave_list= [spaces[i] for i in range(0, len(spaces), 2) if spaces[i+1-2*(((i/2)%3)==1)] and spaces[i+3-(i>4)*6] if i!=4]
                #List of diagnonal spaces that have two 1 adjacent spaces on either side (thus it has varying len)
                new_grid[x][y]= 1+ (sum(concave_list) < len(concave_list))*4 + sum ([len(concave_list) < value_ for value_ in (1,2,4)])
                #Equation to get the points described above
    return new_grid

def draw_lines(grid):
    '''Draws on a pyplot the grid representing present space'''
    for ver_bool in range(2):
        (drawer, grid)=(plt.vlines, invert_grid(grid)) if ver_bool else (plt.hlines, grid)

        for row_num, row in enumerate(grid):
            for cell_num in range(len(row)):
                if row[cell_num]>1:
                    end= find_end(row, cell_num)
                    drawer(row_num, cell_num, end-1, linewidth=5, color='r')

def find_end(row, i, ends=[0]):
    '''Returns index of nearest end of a given value or last possible node if closer '''
    return min([len(row)] + [i+row[i:].index(end) +bool(end) for end in ends if end in row[i:]])

def invert_grid(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
    



def find_corresponding_concave_points(grid, line_dict={}, nodes=[]):
    '''Finds all the pairs concave points (in between 5-7 on graph) in which a straight line can be drawn between 
    on only 1s (i.e. not an edge).  First horzontal, then vertical. Returns as set of Node objects.  
    Finds all intersections and records in Node object.'''
    for ver_bool in range(2):
        #First 0 or horizontal and then 1, veertical
        if ver_bool: grid= invert_grid(grid)
        for axis_line in range(len(grid)):
            for corr_left in range(len(grid[0])):
                if 4<grid[axis_line][corr_left]<8 and (axis_line, corr_left, ver_bool) not in line_dict:
                    end= find_end(grid[axis_line], corr_left, [0]+range(2, 5))
                    corr_right= max([0]+[j for j in range(corr_left+1, end) if grid[axis_line][j] in range(5,8)])
                    if corr_right and (1 in grid[axis_line][corr_left:corr_right]): 
                        node=Node(ver_bool, axis_line, corr_left, corr_right)
                        nodes.append(node)
                        for spot in range(corr_left+1, corr_right):
                            if ver_bool and (spot, axis_line, 0) in line_dict: 
                                #If vertical and point is in keys of line as horizontal
                                node.addlink(line_dict[(spot, axis_line, 0)])
                            line_dict[(axis_line, spot, ver_bool)]=node
    return set(nodes)


def find_corners(new_grid):
    '''Returns all the corners in a given transformed grid'''
    corner_dict={}
    corners= [(x, y) for x in range(len(new_grid)) for y in range(len(new_grid[x])) if new_grid[x][y] is 3]
    for corner in corners:
        '''Searches all 3's (corners) and identifies those forming bottom-left corner of rect, then finds closest respective point''' 
        x,y=corner
        for side in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
            hor, ver= side 
            if x+hor <len(new_grid) and y+ver<len(new_grid[0]) and (new_grid[x+hor][y] and new_grid[x][y+ver]) is 2: 
                corner_dict[corner]= ("right", "left")[side[1]] + ("top", "bottom")[side[0]]
            
            # 3's all bounded by two twos on adjacent sides--which sides reflects what corner of rect
    return corner_dict


def add_lines(grid, table, count=0):
    '''Adds nodes in maximum set to grid as edges and draws them on pyplot in blue. Also returns lines drawn'''
    for node in table.nodes:
        if node in table.max_set:
            count+=1
            (drawer, grid_form)=(plt.vlines, invert_grid(grid)) if node.vertical else (plt.hlines, grid)
            drawer (node.axis_fixed, node.pointa, node.pointb, linewidth=2, color='b')
            grid_form[node.axis_fixed][node.pointa:node.pointb+1]=[3]+[2]*(node.pointb-node.pointa-1)+[3]
            if node.vertical: grid=invert_grid(grid_form)
    return grid, count

def draw_new_lines(grid, count=0):
    '''Draws lines on pyplot and on grid as edges.  Returns grid and total number of drawn lines'''   
    for ver_bool in (0,1):
        (drawer, grid_form)=(plt.vlines, invert_grid(grid)) if ver_bool else (plt.hlines, grid)
        for row_num, row in enumerate(grid_form):
            for cell_num in range(len(grid_form[0])):
                if row[cell_num] in range(5,8) and 0<cell_num-1< cell_num+1<len(row):
                    behind, cell, ahead =row[cell_num-1:cell_num+2]
                    two_behind, two_ahead= [row[cell_num+2*i] if 0<=cell_num+2*i<len(row) else None for i in (-1,1)]
                    actual_concave_corner = lambda forward, backward, forward_2: \
                    (forward is 1 or (backward is 2 and forward_2 is 0)) and backward is not 4
                    if actual_concave_corner(ahead, behind, two_ahead):
                        '''Draws lines between points if across rect (however short i.e. no middle 1 e.g. 0520), 
                        not if from a concave point formed from a double edge (4)'''
                        begin, end= cell_num, find_end(row, cell_num, [0,2])-1
                    elif actual_concave_corner(behind, ahead, two_behind):
                        #Draws backwards (right to left or top down) as well
                        begin, end= len(row)- find_end(list(reversed(row)), len(row)-cell_num, [0,2]), cell_num
                    else: continue
                    drawer(row_num, begin, end, linewidth=2, color='b')
                    grid_form[row_num][begin:end+1] = [2]*(end-begin+1)
                    if ver_bool: grid=invert_grid(grid_form)

    return grid, count 


def draw_nodes(nodes, color='g'):
    for node in nodes:
        drawer = plt.vlines if node.vertical else plt.hlines
        drawer (node.axis_fixed, node.pointa, node.pointb, linewidth=2, color=color)
    






