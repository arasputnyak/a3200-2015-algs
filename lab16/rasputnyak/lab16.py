import heapq

class Vertex:
    def __init__(self, ind):
        self.ind = ind
        self.parent = None
        self.path = None
        self.weight = {}
        self.adj = []

    def __lt__(self, other):
        return self.path < other.path

class WeightedGraph:
    def __init__(self):
        self.V = []
        
    def add_vertex(self, v):
        vertex = Vertex(v)
        self.V.append(vertex)

    def add_direct_link(self, vert1, vert2, weight):
        v1 = self.V[vert1]
        v2 = self.V[vert2]
        v1.weight[v2] = weight
        v1.adj.append(v2)
    
    def initialize(self, s):
        for i in range(len(self.V)):
            self.V[i].path = 1000 ** 10
            self.V[i].parent = None
        s.path = 0

    def relax(self, v1, v2):
        w = v1.weight[v2]
        if v2.path > v1.path + w:
            v2.path = v1.path + w
            v2.parent = v1

    def vertex_sort(self, lst):
        minimum = lst[0]
        for i in range(1, len(lst)):
            if lst[i].path < minimum.path:
                lst[i], minimum = minimum, lst[i]
                minimum = lst[i]

    def Dijkstra(self, t):
        self.initialize(t)
        S = []
        Q = []
        for i in range(len(self.V)):
            Q.append(self.V[i])
        heapq.heapify(Q)
        while len(Q) > 0:
            v1 = heapq.heappop(Q)
            S.append(v1)
            for i in range(len(v1.adj)):
                self.relax(v1, v1.adj[i])

    def shortest_path(self, vert1, vert2):
        v1 = self.V[vert1]
        v2 = self.V[vert2]
        self.Dijkstra(v1)
        path = []
        x = v2
        err = 0
        while x != v1:
            path.append(x.ind)
            if x.parent == None:
                print("no path")
                err = 1
                break
            x = x.parent
        if err == 0:
            path.append(x.ind)
            path.reverse()
            return path
        else:
            path.clear()
            return path


