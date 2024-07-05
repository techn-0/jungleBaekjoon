def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] >arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(len(arr)):
        print(arr[i])
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
bubble(arr)