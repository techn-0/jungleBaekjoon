def solution(s):
    # s = list(s)
    answer = 0
    negative = False
    
    if s[0] == "-":
        negative = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]
    answer = int(s)
    if negative:
        answer = 0-answer
    
    return answer