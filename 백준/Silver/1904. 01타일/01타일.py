N = int(input())

arr = []
arr.append(0)
arr.append(1)

for i in range(2, N + 2):
    arr.append((arr[i - 1] + arr[i - 2]) % 15746)

print(arr[N + 1])