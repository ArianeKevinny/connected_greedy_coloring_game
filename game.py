from structs import Graph;

## Strategic: MinMax

## Initialize: graph

edges = [(1, 2), (1, 5), (1, 4), (2, 3), (3, 6), (4, 6), (4, 5), (4, 7), (4, 8), (5, 7), (6, 8), (7, 8), (7, 9), (7, 10), (8,9), (9, 11), (10, 11)];
print("The planar graph has "+str(len(edges))+" edges");
planar_graph = Graph(edges);

edges = [(1, 2), (1, 3), (1, 4), (3, 5), (3, 6)];
print("The tree has "+str(len(edges))+" edges");
tree_graph = Graph(edges);

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)];
print("The cycle has "+str(len(edges))+" edges");
tree_graph = Graph(edges);



