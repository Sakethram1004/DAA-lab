n = 5  
matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

def to_be_visited():
    global visited_and_distance
    v = -10
    for index in range(n):
        if visited_and_distance[index][0] == 0 and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
            v = index
    return v

visited_and_distance = [[0, 0]]
for i in range(n - 1):
    visited_and_distance.append([0, 999999])

for vertex in range(n):
    to_visit = to_be_visited()

    for neighbor_index in range(n):
        if matrix[to_visit][neighbor_index] > 0 and visited_and_distance[neighbor_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] + matrix[to_visit][neighbor_index]
            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance

    visited_and_distance[to_visit][0] = 1

i = 0
print("Dijkstra Algo output: ")
for distance in visited_and_distance:
    print("Distance of", i, "from source vertex:", distance[1])
    i += 1
