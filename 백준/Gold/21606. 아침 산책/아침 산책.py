import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

io = input().rstrip()

graph = [[]for _ in range(N + 1)]
visited = [0] * (N+1)
place = [0] * (N+1)

for i in range(len(io)):
    if io[i] == '1':
        place[i+1] = 1

for _ in range(N -1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def dfs(node):
    res = 0
    for i in graph[node]:
        if place[i] == 0:
            if not visited[i]:
                visited[i] = 1
                res += dfs(i)
        else:
            res += 1
    return res

ans = 0
for i in range(1, N+1):
    if place[i] == 0:
        if not visited[i] == 1:
            visited[i] = 1
            res = dfs(i)
            ans += res * (res -1)
    else:
        for j in graph[i]:
            if place[j] == 1:
                ans += 1
print(ans)