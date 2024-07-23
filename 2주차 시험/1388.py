import sys
from collections import deque
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1
    if arr[x][y] =='|':
        if x + 1 < N and  arr[x + 1][y] =='|' and visited[x+1][y] == 0:
            dfs(x + 1, y)
        else:
            return
    if arr[x][y] == '-':
        if y + 1 < M and  arr[x][y + 1] =='-'and visited[x][y+1] == 0:
            dfs(x, y + 1)
        else:
            return

N, M = map(int, input().split())
arr = []
count = 0

visited = []
temp = [0] * M
for _ in range(N):
    visited.append(temp[:])

for _ in range(N):
    arr.append(list(input()))

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)