def solution(a, b):
    answer = 0
    if a==b:
        return a
    if a > b:
        s = b
        e = a
    else:
        s = a
        e = b
    for i in range(s, e+1):
        answer += i
    return answer