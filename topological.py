class Graph:
    def __init__(self, V, adj):
        self.V = V
        self.Matrix = adj

    def topological_sort(self):
        indegree = [0] * self.V
        for x in range(self.V):
            for y in range(self.V):
                indegree[y] += self.Matrix[x][y]

        queue = []
        order = []
        visited = []

        for x in range(self.V):
            if indegree[x] == 0:
                queue.append(x)
                visited.append(x)

        while queue:
            u = queue.pop(0)
            order.append(u)

            for x in range(self.V):
                indegree[x] -= self.Matrix[u][x]
                self.Matrix[u][x] = 0

            for x in range(self.V):
                if indegree[x] == 0 and x not in visited:
                    queue.append(x)
                    visited.append(x)

        print("Topological order is:", order)

# Example usage
n = int(input("Enter the number of vertices: "))
adj = [[0] * n for _ in range(n)]

for i in range(n):
    print("Enter the dependencies of %d DLL with other DLLs (if no dependency, click enter)" % (i))
    l = [int(x) for x in input().split()]
    
    for j in l:
        adj[j][i] = 1

G = Graph(n, adj)
print(G.Matrix)
G.topological_sort()
