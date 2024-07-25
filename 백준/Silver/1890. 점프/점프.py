import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
gamebord = []
for _ in range(N):
    gamebord.append(list(map(int, input().split())))


dp = [[-1] * N for _ in range(N)]

mov = [(1,0),(0,1)]

def DFS(x, y):
    if x == N-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for i in mov:
            nx = x + i[0] * gamebord[x][y]
            ny = y + i[1] * gamebord[x][y]
            if 0 <= nx < N and 0 <= ny < N:
                dp[x][y] += DFS(nx,ny)
    return dp[x][y]

print(DFS(0,0))