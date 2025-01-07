def solution(N):
    num = format(N, 'b')
    maxgap = 0
    cur = 0
    for i in num:
        if i == '1':
            maxgap = max(maxgap, cur)
            cur =0
        else:
            cur += 1
    return(maxgap)