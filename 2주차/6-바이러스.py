import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]
visited =[0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(graph, v, visited):
    global count
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
            count += 1

dfs(graph, 1, visited)
print(count)