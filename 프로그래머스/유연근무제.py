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
# -------------------------------------

# 출근 인정 시간이 올바르게 변환되지 않음 (59분 문제)
# 59분에 출근 인정 시간인 +10을 해주면 69가 되는데 60분이 넘어가게 되면 시간으로 넘겨주는 작업을 해 주어야 함
# 시간 처리를 하는 함수를 따로 분할하여 모듈화 하자

# 모든 요일을 확인하지만, 평일 5일만 체크해야 함
# 주말이면 요일 카운트만 올리고 다음 인덱스로 넘어가야 함

# 출근 기록이 부족한 경우 실패 처리 필요
# 출근한 날짜가 5일 미만이라면 False 처리 해주어야 함