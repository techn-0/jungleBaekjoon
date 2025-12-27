def solution(x):
    answer = True
    div = 0
    l = len(str(x))
    
    for i in range(1, l+1):
        div += (x % (10**i))//10**(i-1)
    if x % div != 0:
        answer = False
    return answer