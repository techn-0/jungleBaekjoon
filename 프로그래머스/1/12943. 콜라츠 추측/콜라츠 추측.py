def solution(num):
    def runEven(n):
        n = n // 2
        return n
    def runOdd(n):
        n = n*3+1
        return n
    def isEven(n):
        if n % 2 == 0:
            return True
    cnt = 0
    while num != 1:
        if isEven(num):
            num = runEven(num)
        else:
            num = runOdd(num)
        cnt +=1
        if cnt >=500:
            return -1
    answer = cnt
    
    
    return answer
