def solution(a, b):
    answer = 0
    l = len(a)
    sum = 0
    for i in range(l):
        n1 = a[i]
        n2 = b[i]
        tmp = n1 * n2
        answer += tmp
    return answer