class Graph:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph

    def printMST(self, parent):
        print("Edge\tWeight")
        total = 0
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
            total += self.graph[i][parent[i]]
        print("Min length connecting all devices: ", total)

    def minKey(self, key, mstSet):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


n = int(input("Enter the number of Vertices: "))
matrix = [
    [0, 2, float('inf'), 6, float('inf')],
    [2, 0, 3, 8, 5],
    [float('inf'), 3, 0, float('inf'), 7],
    [6, 8, float('inf'), 0, 9],
    [float('inf'), 5, 7, 9, 0]
]

g = Graph(n, matrix)
g.primMST()
