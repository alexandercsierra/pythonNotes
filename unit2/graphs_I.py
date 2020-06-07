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