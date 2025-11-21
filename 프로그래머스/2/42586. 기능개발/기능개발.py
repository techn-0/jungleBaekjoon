def solution(progresses, speeds):
    answer = []
    
    n = len(progresses)
    
    # 100에서 진행도를 빼고 남은 숫자를 보자
    doneDay = []
    for i in range(n):
        m = 100 - progresses[i]
        s = speeds[i]
        doneDay.append((m + s -1)//s)
    # print(doneDay)
    
    cnt = 1
    day = doneDay[0]
    
    for i in range(1, n):
        if doneDay[i] <= day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = doneDay[i]
    answer.append(cnt)
    return answer