# Assuming matrix is the adjacency matrix of the graph
matrix = [
    [0, 2, float('inf'), 6, float('inf')],
    [2, 0, 3, 8, 5],
    [float('inf'), 3, 0, float('inf'), 7],
    [6, 8, float('inf'), 0, 9],
    [float('inf'), 5, 7, 9, 0]
]

n = len(matrix)
a = [row[:] for row in matrix]

for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j] = min(a[i][j], a[i][k] + a[k][j])

print("Min distance between two devices using Floyd-Warshall: ")
for row in a:
    print(row)
