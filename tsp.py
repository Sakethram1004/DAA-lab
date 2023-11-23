def g(vertex, rem_v):
    if not rem_v:
        return w[vertex][0]
    elif (vertex, tuple(rem_v)) in memo:
        return memo[(vertex, tuple(rem_v))]
    else:
        mi = float('inf')
        ind = 0
        for i in rem_v:
            temp = rem_v.copy()
            temp.remove(i)
            val = w[vertex][i] + g(i, temp)
            if val < mi:
                mi = val
                ind = i
        memo[(vertex, tuple(rem_v))] = mi
        index[(vertex, tuple(rem_v))] = ind
        return mi

def path(vertex, rem_v, r):
    if not rem_v:
        r.append(vertex + 1)
        r.append(1)
    else:
        r.append(vertex + 1)
        ind = index[(vertex, tuple(rem_v))]
        rem_v.remove(ind)
        path(ind, rem_v, r)
    return r

v = int(input('Number of objects: '))
w = []

print('Enter slewing time for travel from each object to all other objects:')
for i in range(v):
    l = input('{}->'.format(i + 1))
    l = list(map(int, l.split(',')))
    w.append(l)

memo = {}
index = {}

for i in range(1, len(w)):
    memo[(i, ())] = w[i][0]

print("The min cost: ", g(0, [x for x in range(1, len(w))]))
print("The required path is: ", path(0, [x for x in range(1, len(w))], []))
