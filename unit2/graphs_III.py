'''
Connected components are nodes connected by edges
-parts of the graph that are connected, but disjointed from other parts of the graph (island)

How to find connected components and visit all nodes?
-Create set of all nodes
-chose starting node
-do search
-pick a node that wasn't in visited
-restart
(see connected_components image)
'''

'''
For each node:
    if node not visited:
        traverse from that node (mark as visited)
        increment counter
'''

'''
In a matrix, nodes are connected in an island if there is a 1 directly above, below, left, or right (not diagonal)

(not the same as an adjacency matrix. This one marks nodes not connections)


for each node:
    if node not visited and the node is 'land':
        traverse from that node
        increment counter

'''

islands = [
    [0,1,0,1,0],
    [1,1,0,1,1],
    [0,0,1,0,0],
    [1,0,1,0,0],
    [1,1,0,0,0]
]

def island_counter(matrix): #matrix is a 2d array
    visited = []
    island_count = 0
    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
    
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    dft(row, col, matrix, visited)
                    island_count +=1
    return island_count

def get_neighbors(row, col, matrix):
    neighbors = []

    #check n s e w
    #north
    #check if in range
    if row > 0 and matrix[row-1][col] ==1:
        neighbors.append((row-1, col))
    #south
    if row < len(matrix)-1 and matrix[row+1][col] ==1:
        neighbors.append((row+1, col))
    #west
    if col > 0 and matrix[row][col-1] ==1:
        neighbors.append((row, col-1))
    #east
    #square matrix means columns same at any point, so just pick 0
    if col < len(matrix[0])-1 and matrix[row][col+1] ==1:
        neighbors.append((row, col+1))

    return neighbors


def dft(row, col, matrix, visited):
    s = []
    s.append((row, col))

    while len(s) > 0:
        #destructuring
        row, col = s.pop()

        if not visited[row][col]:
            visited[row][col] = True

            for neighbor in get_neighbors(row, col, matrix):
                s.append(neighbor)


print(island_counter(islands)) #4
    #create a visited matrix
    #walk through each cell in the matrix
        #if it's not been visited
            #if it's a 1
                #do a dft and mark them as visited
                #increment counter by 1
    #return counter




class Graph:

    def populate_graph(self, num_users, avg_friendships):
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.addUser(f'User {i}')

        #generate all possible friendships
        #shuffle all possible friendships
        #go through the list of shuffled frienships, adding the right number of them to reach the avg_friendships