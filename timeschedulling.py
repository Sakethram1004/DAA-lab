n = int(input("Enter the number of subjects: "))
sub = []

for i in range(n):
    print("Enter subject_code and subject_name for {}".format(i + 1))
    l = list(map(str, input().split()))
    sub.append(l)

print(sub)

x = [0 for _ in range(n)]
G = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    print("Enter clashes for subject {}".format(i + 1))
    l = list(map(int, input().split()))

    for j in l:
        G[i][j - 1] = 1

print(G)

def time_scheduling(k, i):
    while i:
        next_value(k)
        if x[k] == 0:
            return
        if k == n - 1:
            print("Time line schedule sequence is:", *x)
            exit(0)
        i = time_scheduling(k + 1, i)

def next_value(k):
    while True:
        x[k] = (x[k] + 1) % (max(x) + 1)
        if x[k] == 0:
            return
        for j in range(n):
            if G[k][j] != 0 and x[k] == x[j]:
                break
        if j == n - 1:
            return

time_scheduling(0, True)
