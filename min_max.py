import copy
from structs import Graph
from structs import ColoredVertices
from structs import GameTree

def MinMax(G, tree_game, coloreds, k, minmax):

    for v in G.get_neighborhoods_not_colored(coloreds.vertices):
        coloreds_v = copy.deepcopy(coloreds)
        color = coloreds_v.get_min_color(G.get_neighborhoods(v), k)
        coloreds_v.add_vertex(v)
        coloreds_v.add_color(v, color)
        tree_game.add_vertex(coloreds_v) 
        tree_game.add_edge(coloreds, coloreds_v, v)

        if color == -1:  # Caso: não consegui colorir
            if minmax == "MIN":
                tree_game.vertices[coloreds_v] = 0
                tree_game.vertices[coloreds] = 0
                return 0
            else:
                tree_game.vertices[coloreds_v] = 0
                continue
        
        if len(coloreds_v) == len(G):  # Caso: consegui colorir completamente
            tree_game.vertices[coloreds_v] = 1
            if minmax == "MAX":
                tree_game.vertices[coloreds] = 1
                return 1

        if minmax == "MAX":
            result = MinMax(G, tree_game, coloreds_v, k, "MIN")
            tree_game.vertices[coloreds] = max(tree_game.vertices[coloreds_v], result)
        else:
            result = MinMax(G, tree_game, coloreds_v, k, "MAX")
            tree_game.vertices[coloreds] = min(tree_game.vertices[coloreds_v], result)


    return tree_game.vertices[coloreds]

def connected_greedy_coloring_game(G, k):
    tree_game = GameTree()
    coloreds = ColoredVertices()
    tree_game.add_vertex(coloreds)
    result = MinMax(G=G, tree_game=tree_game, coloreds=coloreds, k=k, minmax="MAX")

    return result

