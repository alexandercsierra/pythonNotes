'''
Graphs are nodes connected by edges
can be directed or undirected
    directed allows you to move in a specific directional path from one node to others
    undirected means you can can go in any direction (no arrows)
can be cyclic or acyclic
    start with one node, follow the arrows, and end up back at that node
    if the above can be done anywhere on the graph, it is cyclic

    acyclic does not allow for the above
    you cannot link back to the starting node

    any graph with a bidrectional edge could be considered a cyclic graph
    but cyclic/acyclic is usually only used to describe directional graphs (because in an undirected graph you can go back and forth wherever you want)


can be dense or sparse (subjective, no official cutoff)
    subway map is considered a sparse graph
        stations are the verts/vertices/nodes and the tracks are the edges
        in a sparse graph, a vertex is connected to only a few other verticies. One subway station is likely only connected to two others.

    Delta's flight map could be considered a dense graph
        each airport has many different destinations to fly to
        each vertex is connected to many other vertices.

completely connected graph - when every single node is connected to every single other node


Graph weights
    weighted vs unweighted

    unweighted graphs have edges that all have the same weight

    weighted graphs have unequally weighted paths
        this could represent the cost of any particular path, or the distance between nodes
        it is abstract and could really represent anything (road smoothness, number of hills, train fare, etc)

'''


#representing graphs: adjacency matricies and adjacency lists

class Linked_List_Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Graph_Node:
    def __init__(self, value):
        self.value = value
        self.edges = [] #adjacency list

#adjacency list could be a dictionary of connections for example:

# {
#     A: [B],
#     B: [A, X, P, T]
# }
'''
adjacency matrix is a 2d array containing info about all the connections

adj list would be more relevant in a sparse graph, since we are only listing things that are connected. If we represented a sparse graph with a matrix we would have a lot of empty slots since it has to list all the nodes.

adj matrix would be more relevant in a dense graph, since you can easily represent multiple connections without repeating so many times as in a list

matrix also allows for additional info to be stored, perhaps edge weights instead of just 1s and 0s. 

time to look up a connection would be O(n) in a list, O(1) in a matrix
'''

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() #set of edges

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        #breadth-first traversal
        q = Queue()
        q.enq(starting_vertex_id)

        #keep track of visited nodes
        visited = set()

        #repeat until queue is empty
        while q.size() > 0:

            #deq the first vert
            v=q.deq()

            #if it's not visited:
            if v not in visited:
                print(v)
                #mark as visited
                visited.add(v)

                for nex_vert in self.get_neightbors(v):
                    q.enq(next_vert)

g = Graph()

g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)

g.add_edge(99, 3)
g.add_edge(99, 3490)
g.add_edge(3, 99)

print(g.get_neighbors(99))
print(g.get_neighbors(3))


'''
Breadth-First Traversal

add starting node to a queue
(stack would allow for depth-first traversal)

while queue isn't empty:
    dequeue the first vert
    if that vert isn't visited:
        mark as visited
        add all its unvisited neighbors to the queue

'''

'''
Depth-First Traversal

add starting node to a stack

while stack isn't empty:
    pop the first vert
    if that vert isn't visited:
        mark as visited
        push all its unvisited neighbors to the stack
'''


