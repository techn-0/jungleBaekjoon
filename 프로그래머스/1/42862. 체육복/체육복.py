def solution(n, lost, reserve):
    answer = 0
    safe = n
    lost.sort()
    
    temp = []
    # 여분 있는 사람이 도난당함
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -1
            
            
    
    #빌리기
    for i in lost:
        if i == -1:
            continue
        # 앞뒤사람에게 빌릴수 있음
        elif i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            safe -= 1    
    return safe