def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * fact(n-1)
N = int(input())
print(fact(N))