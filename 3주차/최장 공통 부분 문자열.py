s1 = list(input())
s2 = list(input())
arr = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

max_len = 0
end_pos_s1 = 0

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            arr[i][j] = arr[i-1][j-1] + 1

            if arr[i][j] > max_len:
                max_len = arr[i][j]
                end_pos_s1 = i

        else:
            arr[i][j] = 0

ans = s1[end_pos_s1 - max_len:end_pos_s1]
print(max(map(max, arr)))
print(ans)
