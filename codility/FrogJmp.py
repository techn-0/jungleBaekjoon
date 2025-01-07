def solution(X, Y, D):
    load = Y - X
    cnt = load // D
    if load % D != 0:
        cnt +=1
    return cnt