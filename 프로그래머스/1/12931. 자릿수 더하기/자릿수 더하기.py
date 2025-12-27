def solution(n):
    answer = 0
    
    l = len(str(n))
    
#     한글자 일때 바로 반환
    if l == 1:
        return n
#     두 글자 이상일 땐 나누는 수에 10 씩 곱해가며 자리수 별 숫자 찾기
    for i in range(1, l+1):
        num = 10**i
        tmp = int((n % num)/10**(i-1))
        answer += tmp
    return answer