s1 = list(input())
s2 = list(input())
arr = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
print(max(map(max, arr)))
# 직전 비교치가 아니라 이전 열에서 구했던 가장 긴 문자열 중에서
# 갈수있는 경우의수가 뻗어 나가면서 가장 길이가 긴거 하나를 구해야함
# 따라서 대각선 위에값에 +1