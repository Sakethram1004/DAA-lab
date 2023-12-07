from numpy import array

class Item:
    def __init__(self, price, weight, x):
        self.price = price
        self.weight = weight
        self.x = x

def merge(l, low, high, mid):
    temp = sorted(l[low:high+1], key=lambda item: item.price/item.weight)
    l[low:high+1] = temp

def merge_sort(l, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(l, low, mid)
        merge_sort(l, mid + 1, high)
        merge(l, low, high, mid)
    return l

def knapsack(l, m):
    u = m
    vector = [0] * len(l)

    for i in range(len(l)):
        if u - l[i].weight > 0:
            vector[i] = 1
            l[i].x = 1
            u -= l[i].weight
        else:
            if i < len(l) and u > 0:
                s = (u) / l[i].weight
                vector[i] = round(s, 2)
                l[i].x = vector[i]
                break
    return vector
# Input
n = int(input("Input the size of array: "))
l = [Item(int(input("Price: ")), int(input("Weight: ")), 0) for _ in range(n)]
s = list(l)
m = int(input("Enter the max capacity: "))

# Execution
merge_sort(l, 0, len(l) - 1)
result = knapsack(l, m)

profit = sum(item.price * result[i] for i, item in enumerate(l))
arr = [item.x for item in s]

# Output
print("The result vector x is:", arr)
print("The max profit is obtained:", profit)
