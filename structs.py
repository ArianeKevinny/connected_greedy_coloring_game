#The graph
from collections import defaultdict

class Graph(object):

    def __init__(self, edges, directed=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.directed = directed
        self.add_edges(edges)

    def get_vertices(self):
        return list(self.adj.keys())
    
    def get_neighborhoods(self, v):
        if (v == "root"):
            return self.get_vertices()
        if v in self.adj.keys:
            return list(self.adj[v])
        else:
            return []
    def get_connected(self, coloreds):
        
        if (coloreds == "root"):
            return self.get_vertices()
        else:
            list = defaultdict(set)
            for v in coloreds:
                if v in self.adj.keys:
                    for u in self.adj[v]:
                        if u not in coloreds:
                            list.add(u)
            return list

    def get_edges(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def add_edges(self, edges):
        for u, v in edges:
            self.adj[u].add(v)
            if not self.directed:
                self.adj[v].add(u)
       
    def exist_edge(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]
        
    def __del__(self):
        print('Destructor invoked, graph removed.')

def show_graph(G):
    #Trabalhar nisso
    return 0  

class ColoredVertices:

    def __init__(self):
        """Inicializa as estruturas base do grafo."""
        self.vertices = defaultdict(set)
        self.color ={}


    def get_vertices(self):
        return list(self.adj.keys())
    
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    
    def add_color(self, vertex, color):
        self.color[vertex] = color

    def get_min_color(self, neighborhoods, k):
        colors = defaultdict(set)
        for u in neighborhoods:
            if u in self.vertices.keys():
                colors.add(self.color[u])

        for i in range(1, k+1):
            if i not in colors: 
                return i
        
        return -1

class GameTree:

    def __init__(self, data=-1):

        self.data = data
        # Lose: 0, Win: 1, default:-1 
        self.vertices = {}
        self.edges = {}
    
    def add_vertex(self, u, data=-1):
        self.vertices[u] = data;
        # Lose: 0, Win: 1, default:-1 

    def add_edge(self, u, v, data):
        #Data se refere ao vértice escolhido do grafo 
        self.edges[(u,v)] = (data)

    def remove_vertex(self, u):
        edges = []
        for edge, _ in self.edges.items():
            if u in edge:
                edges.append(edge)

        for edge in edges:
            del self.edges[edge]
        
        del self.vertices[u]