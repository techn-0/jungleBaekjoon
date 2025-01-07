def solution(A):
    check = 0
    for i in A:
        check ^= i
    return check

