N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
# A[i]과 다음값 크기를 비교해 높으면  i = 다음 인덱스 아니면 다음거
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))