N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

for i in B:
    ch = 0
    for j in A:
        if i == j:
            ch = 1
            break
    if ch == 1:
        print(1)
    else:
        print(0)