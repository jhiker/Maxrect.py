#! /usr/bin/env python

#MAXRECT Author Jonathan Leslie, MIT License

'''Creates BipartiteTable and Node Objects; methods according to Kopft algorithm for 
their maximum matching, minimum vertex cover, and maximum independent set. '''


class BipartiteTable(object):
    def __init__(self, node):
        '''Initiated from a node object'''
        self.max_set=set()
        self.nodes= node.build_graph_from_node(set())
        self.vertex_cover=set()

    def matching_algo(self):
        if len(self)==1: 
            self.max_set=self.nodes
            return
        self.fill_initial() #Find initial solution
        self._refine() #Run Agumenting path until no longer possible
        self.find_s_and_t() #Find remaining free vertices
        free_vertices_links=[]
        for vertex in self.start_vertices+self.end_vertices: free_vertices_links.extend(vertex.links)
        #Level one below free vertices on tree
        if free_vertices_links:
            self.find_maxmimum_set(free_vertices_links)
        else:
            self.find_maxmimum_set(self.nodes)
            #Just send all if no depth to tree

    def __str__(self):
        matching= lambda x: "Part of Max Set" if x in self.max_set else "Part of vertex cover"
        columns= tuple([ "\n".join( [str(node)+ matching(node)+ " Matched: " + (str(node.matched is not None)) + '\n' \
                        for node in self.nodes if node.vertical == x]) for x in (0,1)])
        return "Table: \n column hor: %s \n column ver: %s" %  columns

    def __len__(self):
        return len(self.nodes)

    def augmenting_path(self, path_, visited=set()):
        '''Finds a path between free vertices on left side (horizontal) to right (vertical)
            can cross 'backwards' if already matched.  Returns first path found through recursive DFS. 
            If no augmenting path, returns empty list'''
        node=path_[-1]
        start_vertices=[link for link in node.links if link not in visited]
        for link in start_vertices:
            if (node.matched is link)==node.vertical and link not in path_:
                '''Condition is that where link is matched to node is whether or not vertical in order to continue
                also avoiding infinite loops '''
                path_.append(link)
                if link in self.end_vertices:
                    return path_
                return self.augmenting_path(path_, visited)
            else:
                visited.add(link)
        visited.add(path_.pop())
        if path_: 
            return self.augmenting_path(path_, visited)
        return []
        
     
    def _refine(self):
        '''Implements augmenting path algorithm and changes matching state through current state  ^ aug path;
           Repeats until there is no aug path'''
        self.find_s_and_t()
        for start_vertex in self.start_vertices:
            self.aug_path = self.augmenting_path([start_vertex,]) 
            assert len(self.aug_path)%2 is 0 #has to be even number of nodes
            count=0
            while count <  len(self.aug_path)-1:
                node, link=self.aug_path[count:count+2]
                if node.matched is link:
                    node.matched=None
                    count+=1
                else:
                    node.matching(link) 
                    count+=2
                    #Since we are changing matched state of two nodes; we move forward twice
            if self.aug_path:
                self._refine()

    def fill_initial(self):
        '''Finds naive solution to maximum matching problem'''
        for node in self.nodes:
            if not node.matched:
                for link in node.links:
                    if not link.matched:
                        node.matching(link)
                        break

    def find_s_and_t(self):
        '''Finds the free vertices on each side: horizontal and vertical'''
        self.start_vertices, self.end_vertices= [], []
        for node in self.nodes:
            if not node.matched:
                if not node.vertical: 
                    self.start_vertices.append(node)
                else:
                    self.end_vertices.append(node)

    def find_maxmimum_set(self, vertices):
        '''Finds Maximum set through finding min vertex cover with a recursive BFS'''
        next_row =[]
        for vertex in vertices:
            if self.vertex_cover | self.max_set == self.nodes:
                for node in self.nodes:
                    if node in self.max_set and node.matched in self.max_set:
                        self.max_set.remove(node) #Matched nodes both covered by min vertex arbitrarily chosen
                return   
            if not vertex.links <=(self.max_set | self.vertex_cover):
                self.vertex_cover.add(vertex)
                self.max_set |= vertex.links
                self.max_set -= self.vertex_cover
                next_row.extend(list(vertex.links))
        self.find_maxmimum_set(next_row)




class Node(object):
    def __init__(self, vertical, axis_fixed, pointa, pointb):
        self.axis_fixed=axis_fixed 
        self.pointa, self.pointb= pointa, pointb
        self.matched=None
        self.links=set()
        self.vertical=vertical #1 if vertical 0 if hor

    def addlink(self, link):
        assert self.vertical is not link.vertical #Have to be diff types
        self.links.add(link), link.links.add(self)

    def matching(self, link):
        self.matched=link
        link.matched=self

    def __str__(self):
        items = tuple (map(str, (self.vertical, self.pointa, self.pointb, self.axis_fixed, self.links)))
        return "%s Line: %s to %s on %s.  Links: %s. " % items

    def __repr__(self):
        return "%s Line: %s to %s on %s" % tuple (map(str, (self.vertical, self.pointa, self.pointb, self.axis_fixed)))

    def build_graph_from_node(self, table=set()):
        '''BFS that returns table (all related nodes) from a given node'''
        table.add(self)
        for link in self.links:
            if link not in table:
                table.union(link.build_graph_from_node(table))

        return table

def build_table(nodes, tables={}):
    '''Cycles through each node and orders table built from it if not already part of a table'''
    for node in nodes:
        if node not in tables:
            table=BipartiteTable(node)
            for node_in_table in table.nodes:
               tables[node_in_table] = table
    tables=set(tables.values())
    assert sum([len(table.nodes) for table in tables])==len(nodes)
    return tables
