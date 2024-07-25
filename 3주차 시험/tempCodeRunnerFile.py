N = int(input())
str = [0] * N
arr = [0] * N

for _ in range(N):
    str.append(int(input()))

arr[0] = str[0]
arr[1] = str[0] + str[1]
arr[2] = max(str[0] + str[2], str[1] + str[2])

for i in range(3, N):
    arr[i] = max(arr[i - 3] + str[i - 1] + str[i], arr[i - 2] + str[i])
print(arr[N-1])