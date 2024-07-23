# N = int(input())
# arr = []

# for i in range(N):
#     arr.append(list(map(int, input().split())))
# ans1 = 1
# ans2 = 1
# ansSum = 0
# for i in range(N):
#     for j in range(2):
#         ans1 *= arr[i][j]
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]

for term in range(1, N):
    for start in range(N):  # 첫행렬 : i, 끝행렬: i+term
        if start + term == N:  # 범위를 벗어나면 무시
            break

        dp[start][start+term] = int(1e9)  # 지금 계산할 첫행렬과 끝행렬
        
        for t in range(start, start+term):
            dp[start][start+term] = min(dp[start][start+term],
                                        dp[start][t]+dp[t+1][start+term] + arr[start][0]
                                        * arr[t][1] * arr[start+term][1])

print(dp[0][N-1])