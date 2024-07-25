N = int(input())
str = [0] * (N + 2)
dp = [0] * (N + 2)

for i in range(N):
    str[i] = int(input())

dp[0] = str[0]
dp[1] = str[0] + str[1]
dp[2] = max(str[0] + str[2], str[1] + str[2])

for i in range(3, N):
    dp[i] = max(dp[i - 3] + str[i - 1] + str[i], dp[i - 2] + str[i])
# 두 칸 건너뛰고 i-1과 i를 밟는 경우
# 한 칸 건너뛰고 i를 밟는 경우
print(dp[N-1])