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

graph = [[]for _ in range(n)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

counts = 0
visited = [False] * (n)

dfs(graph, 0, visited)
print(counts)