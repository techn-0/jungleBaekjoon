def solution(n):
    answer = ''
    issu = True
    for i in range(n):
        if issu == True:
            answer += "수"
            issu = False
        else:
            answer += "박"
            issu = True
    return answer