class Job:
    def __init__(self, profit, deadline, q_no):
        self.profit = profit
        self.deadline = deadline
        self.q = q_no

def merge(l, low, high, mid):
    i = low
    j = mid + 1
    temp = []
    while (i <= mid and j <= high):
        if (l[i].profit > l[j].profit):
            temp.append(l[i])
            i += 1
        else:
            temp.append(l[j])
            j += 1
    while (i <= mid):
        temp.append(l[i])
        i += 1
    while (j <= high):
        temp.append(l[j])
        j += 1
    for i in range(len(temp)):
        l[low + i] = temp[i]
    return l

def merge_sort(l, low, high):
    mid = (low + high) // 2
    if (low < high):
        merge_sort(l, low, mid)
        merge_sort(l, mid + 1, high)
        merge(l, low, high, mid)
    return l

def job_scheduling(l):
    l = merge_sort(l, 0, len(l) - 1)
    max_deadline = 0
    for i in range(len(l)):
        if l[i].deadline > max_deadline:
            max_deadline = l[i].deadline
    
    x = [None] * (max_deadline)
    i = 0
    k = 0
    while k < len(l):
        ind = l[i].deadline - 1
        k += 1
        if x[ind] is None:
            x[ind] = l[i]
        else:
            count = ind
            for j in range(count):
                ind -= 1
                if ind >= 0 and x[ind] is None:
                    x[ind] = l[i]
                    break
        i += 1
    return x

n = int(input("Enter the no of Jobs: "))
qs = []
print("Enter Pi: profit and Di: deadline for each Ji")
for i in range(n):
    profit, deadline = [int(x) for x in input().split()]
    qs.append(Job(profit, deadline, i + 1))

result = job_scheduling(qs)
total = 0
job_subset = []

for i in range(len(result)):
    if result[i] is not None:
        total += result[i].profit
        job_subset.append(result[i].q)

print("The Jobs subset is:", job_subset)
print("The max profit within deadline is:", total)
