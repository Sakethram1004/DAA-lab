class Item:
    def __init__(self, price, weight, x):
        self.price = price
        self.weight = weight
        self.x = x

def merge(l, low, high, mid):
    temp = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if (l[i].price / l[i].weight) > (l[j].price / l[j].weight):
            temp.append(l[i])
            i += 1
        else:
            temp.append(l[j])
            j += 1
    while i <= mid:
        temp.append(l[i])
        i += 1
    while j <= high:
        temp.append(l[j])
        j += 1
    for i in range(len(temp)):
        l[low + i] = temp[i]

def merge_sort(l, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(l, low, mid)
        merge_sort(l, mid + 1, high)
        merge(l, low, high, mid)

def knapsack(l, m):
    u = m
    total = 0
    vector = [0] * len(l)
    for i in range(len(l)):
        if u - l[i].weight > 0:
            vector[i] = 1
            l[i].x = 1
            u -= l[i].weight
        else:
            if i < len(l) and u > 0:
                s = u / l[i].weight
                vector[i] = round(s, 2)
                l[i].x = vector[i]
                break
    return vector  # Return the result vector

if __name__ == "__main__":
    l = []
    n = int(input("Input the size of array: "))
    for i in range(n):
        price = int(input("Price: "))
        weight = int(input("Weight: "))
        l.append(Item(price, weight, 0))
    
    s = list(l)  # Copy of the original list
    
    m = int(input("Enter the max capacity: "))
    
    merge_sort(l, 0, len(l) - 1)
    
    result = knapsack(l, m)
    
    profit = 0
    for i in range(len(l)):
        profit += l[i].price * result[i]
    
    arr = []
    for i in range(len(s)):
        arr.append(s[i].x)
    
    print("The result vector x is:", arr)
    print("The max profit is obtained: ", profit)
