N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
for i in range(1, N):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j -1], arr[j]
for i in range(N):
    print (arr[i])