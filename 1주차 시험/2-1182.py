import sys
N , S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(N):
    for j in range(0, N):
        if arr[i] != arr[j]:
            if arr[i] - arr[j] == S:
                count += 1
            
print(count)

