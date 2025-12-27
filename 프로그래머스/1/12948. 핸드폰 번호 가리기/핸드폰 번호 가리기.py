def solution(phone_number):
    answer = ''
    l = len(phone_number)
    lastNum = phone_number[-4:]
    print(lastNum)
    answer = "*"*(l-4) + lastNum
    return answer