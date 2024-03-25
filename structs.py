from collections import defaultdict

class Graph(object):

    def __init__(self, edges):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.add_edges(edges)

    def get_vertices(self):
        return list(self.adj.keys())
    
    def get_neighborhoods(self, v):
        if v in self.adj:
            return list(self.adj[v])
        else:
            return []
    
    def get_neighborhoods_not_colored(self, coloreds):
        if len(coloreds) == 0:
            return self.get_vertices()
        else:
            not_colored = set(self.get_vertices()) - set(coloreds)
            neighborhoods = set()
            for v in not_colored:
                if any(u in coloreds for u in self.adj[v]):
                    neighborhoods.add(v)
            return list(neighborhoods)

    def get_edges(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def add_edges(self, edges):
        for a in edges:
            self.adj[a[0]].add(a[1])
            self.adj[a[1]].add(a[0])
       
    def exist_edge(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]

class ColoredVertices:

    def __init__(self):
        """Inicializa as estruturas base do grafo."""
        self.vertices = set()
        self.color = {}

    def get_vertices(self):
        return list(self.vertices)
    
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    
    def add_color(self, vertex, color):
        self.color[vertex] = color

    def get_min_color(self, neighborhoods, k):
        colors = set(self.color[u] for u in neighborhoods if u in self.color)
        for i in range(1, k+1):
            if i not in colors: 
                return i
        return -1
    
    def __len__(self):
        return len(self.vertices)

class GameTree:

    def __init__(self, data=-1):
        self.data = data
        # Lose: 0, Win: 1, default:-1 
        self.vertices = {}
        self.edges = {}
    
    def add_vertex(self, u, data=-1):
        self.vertices[u] = data
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
