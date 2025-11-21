n = int(input())
arr = [1, 1]
for i in range(2, n):
    arr.append(arr[i-1] + arr[i-2])
print(arr[-1])