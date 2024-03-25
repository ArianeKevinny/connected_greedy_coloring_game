from structs import Graph;
from min_max import connected_greedy_coloring_game;

## Strategic: MinMax
## Initialize: graph

edges_1 = [
    (1, 2), (1, 3), (1, 4), (1, 5), (2, 3),
    (2, 5), (3, 4), (4, 5), (4, 6), (5, 6)];
print("The planar graph has "+str(len(edges_1))+" edges");
planar_graph = Graph(edges_1);

edges_2 = [(1, 2), (1, 3), (3, 5)];
print("The tree has "+str(len(edges_2))+" edges");
tree_graph = Graph(edges_2);

edges_3 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)];
print("The cycle has "+str(len(edges_3))+" edges");
cycle_graph = Graph(edges_3);




k=5
result = connected_greedy_coloring_game(planar_graph, k)

print("Alice wins with "+str(k)+" colors in a Tree: "+str(result))
