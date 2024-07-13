def josep(n, k):
    q = [i for i in range(1, n + 1)]
    removed = []
    while len(q) > 1:
        for j in range(1, k + 1):
            temp = q.pop(0)
            if j != k:
                q.append(temp)
        removed.append(temp)
    removed.append(q[0 ])
    return removed

n, k = map(int, input().split())
val = josep(n, k)
print('<', end='')
for i in range(len(val)):
    if i== len(val) - 1:
        print(val[i], end='>')
    else:
        print(val[i], end=', ')