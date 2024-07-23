import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, parent, arr, io):
    global count
    if io[start - 1]:
        for j in arr[start]:
            if io[j-1]:
                count += 1
            else:
                dfs(j, start, arr, io)

N = int(input())
io = input()

arr = [[] for _ in range(N+1)]
for _ in range(N - 1):
    a, b= map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
print(arr)


count = 0


for i in range(1, N+1):
    parent = i
    dfs(i, i, arr, io)

print(count)