def solution(absolutes, signs):
    answer = 0
    l = len(absolutes)
    
    for i in range(l):
        n = absolutes[i]
        if signs[i] == False:
            n = 0-n
        answer += n
            
    return answer