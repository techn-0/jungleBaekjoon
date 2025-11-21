def solution(array, commands):
    answer = []
    
    n = len(commands)
    
    num = 0
    for j in range(n):
        srt , end, target = commands[j]
        # print(srt , end, target)
        temp = sorted(array[srt-1: end])
        answer.append(temp[target-1])
    
    return answer