def josep(n, k):
    q = [i for i in range(1, n + 1)]
    while len(q) > 1:
        for j in range(1, k + 1):
            friend = q.pop(0)
            if j != k:
                q.append(friend)
    return q[0]

n, k = map(int, input().split())
print(josep(n, k))