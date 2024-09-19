from collections import deque

def solution(queue1, queue2):
    answer = 0
    # 큐를 deque로 변환하여 pop(0) 대신 popleft()를 사용해 효율성 향상
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 두 큐의 합을 미리 계산
    a = sum(queue1)
    b = sum(queue2)
    
    total_sum = a + b
    # 두 큐의 합이 홀수면 두 큐의 합을 같게 만들 수 없음
    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    max_operations = len(queue1) * 3  # 최대 이동 횟수는 큐의 길이 * 3 정도로 제한
    
    while a != target and answer < max_operations:
        if a > target:
            num = queue1.popleft()  # queue1에서 값 빼기
            a -= num  # queue1 합계에서 그 값 빼기
            b += num  # queue2 합계에 더하기
            queue2.append(num)  # queue2에 값 추가
        else:
            num = queue2.popleft()  # queue2에서 값 빼기
            b -= num  # queue2 합계에서 그 값 빼기
            a += num  # queue1 합계에 더하기
            queue1.append(num)  # queue1에 값 추가
        answer += 1
    
    if a == target:
        return answer
    else:
        return -1
