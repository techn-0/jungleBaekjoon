import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

arr = []
while 1:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
def div(A):
    if len(A) ==0 :
        return
    
    L, R = [], []
    mid = A[0]

    for i in range(1, len(A)):
        if A[i] > mid :
            L = A[1:i]
            R = A[i:]
            break
    else:#for-else 문으로 쓰인 else 포문 끝까지 수행시 else실행
        L = A[1:]
    div(L)
    div(R)
    print(mid)
div(arr)