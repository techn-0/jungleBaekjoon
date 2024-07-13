import sys

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

p = '('
def valid(arr):
    global p
    l = len(arr)
    total = l**2

    s = 0
    for row in arr:
        s += sum(r for r in row)
    if s == 0 or s == total:
        if arr[0][0]:
            p +='0'
        else:
            p +='1'
    else:
        valid([a[:l//2] for a in arr[:l//2]])
        valid([a[l//2:] for a in arr[:l//2]])
        valid([a[:l//2] for a in arr[l//2:]])
        valid([a[l//2:] for a in arr[l//2:]])

valid(arr)
print('(', end='')
print(p, end='')
print(')')