# The connected greedy coloring game
# This program will simulate the connected greedy coloring game with different values of k.
# The objective of these simulations is to obtain approximate upper limits for the value of K.

# minmax algorithms -< Exist A¹ for all B¹ ... tal que A^n wins with k colors
# So the player Alice is max and Bob is min
import copy

from structs import Graph;
from structs import GameTree;
from structs import ColoredVertices;

edges = [(1, 2), (1, 5), (1, 4), (2, 3), (3, 6), (4, 6), (4, 5), (4, 7), (4, 8), (5, 7), (6, 8), (7, 8), (7, 9), (7, 10), (8,9), (9, 11), (10, 11)];
print("The planar graph has "+str(len(edges))+" edges");
planar_graph = Graph(edges);

edges = [(1, 2), (1, 3), (1, 4), (3, 5), (3, 6)];
print("The tree has "+str(len(edges))+" edges");
tree_graph = Graph(edges);

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)];
print("The cycle has "+str(len(edges))+" edges");
tree_graph = Graph(edges);

def max(G, v, tree_game, coloreds, k):
    
    for u in G.get_neighborhoods(v):
        if u in coloreds.vertices:
            continue
        
        color = coloreds.get_min_color(G.get_neighborhoods(u), k)      
        coloreds.add_vertex(u)
        coloreds.add_color(u, color)
               
        tree_game.add_vertex(coloreds) 
        tree_game.add_edge(v, coloreds, u)

        
        if color == -1:
            #Caso onde não foi possível colorir o vértice com até k cores
            tree_game.vertices[coloreds] = 0
            continue

        min(G, tree_game, coloreds, k)

def min(G, tree_game, coloreds, k):
    
    for u in G.get_connected_not_colored(coloreds.vertices):
        
        coloreds_u = copy.deepcopy(coloreds)

        color = coloreds_u.get_min_color(G.get_neighborhoods(u), k)

        if color == -1:
            #Caso onde não foi possível colorir o vértice com até k cores
            tree_game.vertices[coloreds] = 0
            break

        coloreds_u.add_vertex(u)
        coloreds_u.add_color(u, color)
               
        tree_game.add_vertex(coloreds_u) 
        tree_game.add_edge(coloreds, coloreds_u, u)

        max(G, tree_game, coloreds_u, k)


def connected_greedy_coloring_game(G, k):
  #G is a connected graph and {1, 2, ..., k} is the colors.
    
    #Make the tree_game

    tree_game = GameTree()
    tree_game.add_vertex("root")
    coloreds = ColoredVertices()





    # Primeiras escolhas da alice
        #escolhas do Bob
    
    
    

    
    return 0;