def check(n):
    if int(n) <= 1:
        return False
    for j in range(2, int(n)):
        if int(n) % j == 0:
            return False
    return True
T = int(input())
for i in range(T):
    num = int(input())
    n1, n2 = num // 2, num // 2
    while n1 > 0:
        if check(n1) and check(n2):
            print(n1, n2)
            break
        else:
            n1 -= 1
            n2 += 1