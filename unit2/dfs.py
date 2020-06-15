def dfs_recursive(self, starting_vertex, destination_vertex):
            current_path = starting_vertex
            if type(starting_vertex) == int:
                current_path = [starting_vertex]

            visited_nodes.append(current_path[-1])
            if current_path[-1] == destination_vertex:
                print('in if', current_path)
                return current_path

            print(self.get_neighbors(current_path[-1]))
            for vert in self.get_neighbors(current_path[-1]):
                if vert not in visited_nodes:
                    new_path = [*current_path, vert]
                    print('new_path', new_path)
                    if self.dfs_recursive(new_path, destination_vertex):
                        return self.dfs_recursive(new_path, destination_vertex)
            return None


visited_nodes = []

dfs_recursive(1, 6):
    current_path = 1
    if type(1) == int:
        current_path = [1]

    visited_nodes.append(1)
    if 1 == 6:
        #not true
        return [1]

    for vert in self.get_neighbors(1):
        #verts should be 2
        if 2 not in visited_nodes: # it isn't
            new_path = [1, 2]
            if self.dfs_recursive([1,2], 6):
                return self.dfs_recursive([1,2], 6)
    return


visited_nodes = [1]

dfs_recursive([1,2], 6):
    current_path = [1,2]

    #only relevant first pass
    if type([1,2]) == int:
        current_path = [starting_vertex]

    visited_nodes.append(2)
    if 2 == 6:
        #not true
        return [1,2]

    for vert in self.get_neighbors(2):
        #verts should be 3 and 4
        if 3 not in visited_nodes: # it isn't
            new_path = [1, 2, 3]
            if self.dfs_recursive([1,2,3], 6):
                return self.dfs_recursive([1,2,3], 6)

        if 4 not in visited_nodes: # it isn't
            new_path = [1, 2, 4]
            if self.dfs_recursive([1,2,4], 6):
                return self.dfs_recursive([1,2,4], 6)
    return


visited_nodes = [1, 2]

dfs_recursive([1,2,3], 6):
    current_path = [1,2,3]

    #only relevant first pass
    if type([1,2,3]) == int:
        current_path = [starting_vertex]

    visited_nodes.append(3)
    if 3 == 6:
        #not true
        return [1,2,3]

    for vert in self.get_neighbors(3):
        #verts should be 5
        if 5 not in visited_nodes: # it isn't
            new_path = [1, 2, 3, 5]
            if self.dfs_recursive([1,2,3,5], 6):
                return self.dfs_recursive([1,2,3,5], 6)
    return

dfs_recursive([1,2,4], 6):
    current_path = [1,2]

    #only relevant first pass
    if type(1) == int:
        current_path = [starting_vertex]

    visited_nodes.append(2)
    if 2 == 6:
        #not true
        return [1]

    for vert in self.get_neighbors(2):
        #verts should be 3 and 4
        if 3 not in visited_nodes: # it isn't
            new_path = [1, 2, 3]
            if self.dfs_recursive([1,2,3], 6):
                return self.dfs_recursive([1,2,3], 6)
                
        if 4 not in visited_nodes: # it isn't
            new_path = [1, 2, 4]
            if self.dfs_recursive([1,2,4], 6):
                return self.dfs_recursive([1,2,4], 6)
    return

visited_nodes = [1,2,3]