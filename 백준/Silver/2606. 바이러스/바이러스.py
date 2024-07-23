import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    global counts
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            counts += 1

n = int(input())
m = int(input())

graph = [[]for _ in range(n + 1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

counts = 0
visited = [False] * (n + 1)

dfs(graph, 1, visited)
print(counts)