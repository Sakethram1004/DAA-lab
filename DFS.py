class Graph:
    def __init__(self, vertices, graph):
        # No. of vertices
        self.V = vertices
        self.Time = 0
        self.count = 0
        self.time_ap = 0
        self.graph = graph

    def AP_Visit(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.time_ap
        low[u] = self.time_ap
        self.time_ap += 1

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.AP_Visit(v, visited, ap, parent, low, disc)
                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def Articulation_Point(self):
        visited = [False] * self.V
        d_ap = [-1] * self.V
        low_ap = [-1] * self.V
        parent_ap = [-1] * self.V
        ap = [False] * self.V

        for i in range(self.V):
            if visited[i] == False:
                self.AP_Visit(i, visited, ap, parent_ap, low_ap, d_ap)

        a = ""
        for i in range(self.V):
            if ap[i] == True:
                a += str(i) + " "
        print("The articulation points are: " + a)

graph = {}
n = int(input("Enter the number of cities: "))
for i in range(n):
    key = int(input("Enter the key: "))
    value = list(map(int, input("Enter the value: ").split(",")))
    graph[key] = value

print(graph)
g = Graph(n, graph)
g.Articulation_Point()
