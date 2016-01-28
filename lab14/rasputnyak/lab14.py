class Vertex:
    def __init__(self, ind):
        self.ind = ind
        self.adj = []
        self.color = 0

# 0 - grey, 1 - red, 2 - black

class Graph:
    def __init__(self):
        self.V = []
        self.SORT = []

    def add_vertex(self, v):
        vertex = Vertex(v)
        self.V.append(vertex)

    def add_direct_link(self, vert1, vert2):
        v1 = self.V[vert1]
        v2 = self.V[vert2]
        v1.adj.append(v2)

    def dfs(self, vert):
        v = self.V[vert]
        v.color = 1
        for w in v.adj:
            if w.color == 0:
                self.dfs(w.ind)
            if w.color == 1:
                exit("cycle, sorre(((9")
        v.color = 2
        self.SORT.append(v.ind)


    def top_sort(self, v):
        if len(self.V) == 0:
            return 0
        self.dfs(v)
        for w in self.V:
            if w.color == 0:
                self.dfs(w.ind)
        print(self.SORT)





