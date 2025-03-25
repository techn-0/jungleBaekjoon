def solution(schedules, timelogs, startday):
    n = len(schedules)
    cont = 0
    
    for i in range(n):
        # 현재 직원 출근 희망 시간
        WSTime = schedules[i]
        # 출근 인정 시간(+10)
        PSTime = WSTime + 10
        # 성공실패
        SS = True
        
        day = startday
        for j in timelogs[i]:
            # 평일일때만 진행
            if 1 <= day <= 5:
                if j >PSTime:
                    SS = False
                    break  
            # 일주일 지나갔나 체크
            if day == 7:
                day = 1
            else:
                day += 1
            
        if SS:
            cont += 1
            
    return cont


# 시각 변환식: h시 m분 = h * 100 + m 