"""
Nodes(Vertex) & Edges
Weighted Graph :- Weight associated with any Edge
Unweighted Graph :- No weight associated with any Edge
Undirected Graph :- No direction associated
Directed Graph :- Direction associated with every Edge
Cyclic Graph :- Graph having atleast one Loop
Acyclic Graph :- Graph having no Loop
Tree :-  Acyclic Graph


Graph Types:
    - Directed
        - Weighted
            - Positive
            - Negative
        - Unweighted
    - Undirected
        - Weighted
            - Positive
            - Negative
        - Unweighted

Represent Grapgh using Adjacency Matrix


Sample Graph Repr:

    A - B - D - F
    |   |   |   |
    C - E ------
"""


class Graph():

    def __init__(self, gdict={}):
        self.gdict = gdict

    def add_vertex(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def add_edge():



gdict = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['B', 'C', 'D'],
    'F': ['D', 'E']
}

g = Graph(gdict)
g.add_vertex('F', 'G')

print(g.gdict)
