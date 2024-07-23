import sys
from collections import deque

def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a,b))
    graph[a][b] == 0
    counter = 1

    while q:
        x, y =q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    counter += 1
    return counter





dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

count = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count.append(bfs(graph, i, j))

count.sort()
for i in range(len(count)):
    print(count[i])