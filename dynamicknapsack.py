def dp_knapsack(l, m):
    B = [[0 for i in range(m + 1)] for j in range(len(l) + 1)]

    for i in range(len(l)):
        for t in range(1, m + 1):
            if l[i][0] > t:
                B[i + 1][t] = B[i][t]
            else:
                B[i + 1][t] = max(B[i][t], B[i][t - l[i][0]] + l[i][1])

    print("The table we get from the tabulation method is:")
    for i in range(len(B)):
        print(B[i])

    x = [0 for i in range(len(l))]
    i = len(l)
    k = m
    max_pts = B[i][k]

    while i > 0 and k > 0:
        if B[i][k] != B[i - 1][k]:
            x[i - 1] = 1
            k -= l[i - 1][0]
        i -= 1

    print("The max points is:", max_pts)
    print("The solution vector is:", x)

l = []
m = int(input("Enter the max time: "))
n = int(input("Enter the number of questions: "))
print("Enter the time and points of each question: ")
for i in range(n):
    a, b = [int(x) for x in input().split()]
    l.append([a, b])

dp_knapsack(l, m)
