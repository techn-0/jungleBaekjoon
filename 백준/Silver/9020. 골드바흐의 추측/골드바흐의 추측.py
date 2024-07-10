def prime_ch(num):
    if num < 1:
        return False
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True
n = int(input())
for i in range(n): 
    m = int(input())
    l, r = m//2, m//2
    while True:
        if prime_ch(l) and prime_ch(r):
            print(f'{l} {r}')
            break
        else:
            l -= 1
            r += 1