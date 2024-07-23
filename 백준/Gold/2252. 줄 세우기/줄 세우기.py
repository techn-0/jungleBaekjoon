import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inDeg = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A] .append(B)
    inDeg[B] += 1

q = deque()

for i in range(1, N + 1):
    if inDeg[i] == 0:
        q.append(i)

ans = []

while q:
    s = q.popleft()
    ans.append(s)

    for j in graph[s]:
        inDeg[j] -= 1
        if inDeg[j] == 0:
            q.append(j)
print(*ans, sep=" ")