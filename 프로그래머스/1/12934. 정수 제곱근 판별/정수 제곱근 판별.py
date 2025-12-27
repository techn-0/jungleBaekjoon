def solution(n):
    x = int(n**0.5)
    if x*x != n:
        return -1
    return (x+1)**2