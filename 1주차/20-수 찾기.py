N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))
A.sort()

for num in B:
    lt = 0
    rt = N-1
    ch = 0

    while lt <= rt:
        mid = (lt+rt)//2
        if num == A[mid]:
            print(1)
            ch = 1
            break

        elif num > A[mid]:
            lt = mid + 1

        else:
            rt = mid -1
    if ch == 0:
        print(0)