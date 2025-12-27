def solution(numbers):
    answer = -1
    preset = [0,1,2,3,4,5,6,7,8,9]
    sum = 0
    for i in preset:
        if i not in numbers:
            sum += i
    answer = sum
    return answer