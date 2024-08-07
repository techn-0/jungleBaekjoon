import sys
input = sys.stdin.readline
from collections import deque
def bfs(si, sj, v):
    q = deque()

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()
        # 네방향, 범위내(X), 미방문, >0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if v[ni][nj]==0 and arr[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=1


def solve(): # 1 ~ 900000 년, 전체순회 반복작업
    for year in range(1, 900000):
        # [1] 네방향 0의 개수 카운트
        a_sub = [[0]*M for _ in range(N)]
        for i in range(1, N-1):
            for j in range(1, M-1):
                if arr[i][j]==0:
                    continue
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if arr[ni][nj]==0:
                        a_sub[i][j]+=1

        # [2] 높이 낮추기
        for i in range(1, N-1):
            for j in range(1, M-1):
                if a_sub[i][j]>0:
                    arr[i][j]=max(0, arr[i][j]-a_sub[i][j])

        # [3] 빙산 덩어리 개수 카운트
        v = [[0]*M for _ in range(N)]
        cnt=0
        for i in range(1, N-1):
            for j in range(1, M-1):
                if v[i][j]==0 and arr[i][j]>0:
                    bfs(i, j, v)
                    cnt+=1
                    if cnt>1: # 두 덩어리 이상...
                        return year
        if cnt==0:  # 덩어리개수 0개이면.. stop
            return 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve()
print(ans)