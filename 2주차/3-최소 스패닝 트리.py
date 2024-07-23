import sys
input = sys.stdin.readline

V, E =map(int, input().split())

edges = []
sumCost = 0
parent = [0] * (V+1)
for i in range(1, V + 1):
    parent[i] = i #초기 부모값을 자기 자신으로

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

def findMama(parent, x):
    if parent[x] != x:
        #자기 자신이 아니면 부모의 부모의 부모의...
        parent[x] = findMama(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = findMama(parent, a)
    b = findMama(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(E):
    cost, a, b = edges[i]
    if findMama(parent, a) != findMama(parent,b):
        union(parent, a, b)
        sumCost += cost
print(sumCost)