N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

for i in range(len(A)-1):
    for j in range(len(arr)-1):
        if A[i] == arr[j]:
            print(1)
            break
        else:
            print(0)
        