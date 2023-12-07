class Job:
    def __init__(self, profit, deadline, q_no):
        self.profit, self.deadline, self.q = profit, deadline, q_no

def merge(l, low, high, mid):
    i, j, temp = low, mid + 1, []
    while i <= mid and j <= high:
        temp.append(l[i] if l[i].profit > l[j].profit else l[j])
        i += 1 if l[i].profit > l[j].profit else 0
        j += 1 if l[j].profit > l[i].profit else 0
    temp.extend(l[i:mid + 1])
    temp.extend(l[j:high + 1])
    for i, item in enumerate(temp):
        l[low + i] = item
    return l

def merge_sort(l, low, high):
    mid = (low + high) // 2
    if low < high:
        merge_sort(l, low, mid)
        merge_sort(l, mid + 1, high)
        merge(l, low, high, mid)
    return l

def job_scheduling(l):
    l = merge_sort(l, 0, len(l) - 1)
    max_deadline = max((job.deadline for job in l), default=0)
    x = [None] * max_deadline
    i, k = 0, 0
    while k < len(l):
        ind = l[i].deadline - 1
        k += 1
        if x[ind] is None:
            x[ind] = l[i]
        else:
            count = ind
            for j in range(count, -1, -1):
                if x[j] is None:
                    x[j] = l[i]
                    break
        i += 1
    return x

# Input
n = int(input("Enter the number of Jobs: "))
qs = [Job(*map(int, input("Enter profit, deadline, q_no: ").split())) for _ in range(n)]

# Execution
result = job_scheduling(qs)
total, l = sum(job.profit for job in result if job), [job.q for job in result if job]

# Output
print("The Jobs subset is:", l)
print("The max profit within deadline is:", total)
