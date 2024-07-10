T = int(input())

source = [[None]*T]*T
for i in range(T):
    source[i] = input().split()

count = 0
def checkColor(x, y, n):
    global count
    flag = source[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if source[i][j] != flag:
                num = divide(y, n)
                checkColor(x, y, n // 2)
                checkColor(x, y + n // 2, n // 2)
                checkColor(x + n // 2, y, n // 2)
                checkColor(x + n // 2, y + n // 2, n // 2)
                return
    count += 1

def divide(y, n): # n: T
    ll, rr = y, y + n - 1
    mid = (ll + rr) // 2

    lr = mid
    rl = mid + 1

    return [ll, lr, rl, rr]

checkColor(0, 0, T)
print(count)
