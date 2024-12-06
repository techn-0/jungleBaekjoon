import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

gameboard = []
for _ in range(N):
    gameboard.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(N)]
mov = [(1, 0), (0, 1)]

def DFS(x, y):
    if x == N-1 and y == N-1: # 목표 지점인가?
        return 1
    if dp[x][y] != -1: # 이미 경로가 있다면
        return dp[x][y]
    
    dp[x][y] = 0
    for dx, dy in mov:
        nx = x + dx * gameboard[x][y]
        ny = y + dy * gameboard[x][y]
        if 0 <= nx < N and 0 <= ny < N:# 범위를 벗어나지 않았다면
            dp[x][y] += DFS(nx, ny)
    return dp[x][y]
print(DFS(0, 0))