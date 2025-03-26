def solution(schedules, timelogs, startday):
    def convert_time(time):
        h, m = divmod(time, 100)
        m += 10
        if m >= 60:
            h += 1
            m -= 60
        return h * 100 + m  # 올바른 출근 인정 시간 변환
    
    n = len(schedules)
    cont = 0  # 상품을 받을 직원 수
    
    for i in range(n):
        WSTime = schedules[i]  # 희망 출근 시간
        PSTime = convert_time(WSTime)  # 출근 인정 시간 변환
        is_success = True  
        
        day = startday  
        weekday_count = 0  # 평일 출근 횟수 카운트
        
        for j in timelogs[i]:
            if 1 <= day <= 5:  # 평일만 체크
                weekday_count += 1  
                if j > PSTime:  # 지각한 경우
                    is_success = False  
                    break  
            
            day = 1 if day == 7 else day + 1  # 요일 업데이트
            
            if weekday_count == 5:  # 평일 5일 확인 후 중단
                break
        
        if weekday_count < 5:  # 출근 기록이 부족하면 실패 처리
            is_success = False
        
        if is_success:
            cont += 1  
            
    return cont
