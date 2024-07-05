N = int(input())
arr = input().split()
count = 0
for i in range(N):
    if int(arr[i]) > 1:
        ch = 1
        for j in range(2, int(arr[i])):
            if int(arr[i]) % j == 0:
                ch = 0
                break
        if ch == 1:
            count += 1
print(count)