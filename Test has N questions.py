class Test:
    def __init__(self, p, t, x):
        self.p, self.t, self.x = p, t, x

def merge(l, low, high, mid):
    temp = sorted(l[low:high + 1], key=lambda item: item.p / item.t)
    l[low:high + 1] = temp

def merge_sort(l, low, high):
    mid = (low + high) // 2
    if low < high:
        merge_sort(l, low, mid)
    merge_sort(l, mid + 1, high)
    merge(l, low, high, mid)
    return l

def knapsack(l, m):
    u, total = m, 0
    vector = [1 if u - item.t > 0 else 0 for item in l]
    for i, item in enumerate(l):
        if u - item.t > 0:
            item.x, u = 1, u - item.t
        else:
            item.x = 0
            break
    return vector

# Input
l = [Test(int(input("Points: ")), int(input("Time: ")), 0) for _ in range(int(input("Input the size of array: ")))]
s, m = list(l), int(input("Enter the max marks: "))

# Execution
merge_sort(l, 0, len(l) - 1)
result = knapsack(l, m)

score = sum(item.p * result[i] for i, item in enumerate(l))
arr = [item.x for item in s]

# Output
print("The result vector x is:", arr)
print("The highest possible score is:", score)
