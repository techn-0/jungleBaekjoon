def solution(arr):
    answer = []
    n = len(arr)
    
    
    cur = arr[0]
    answer.append(cur)
    for i in range(1, n):
        if cur != arr[i]:
            answer.append(arr[i])
        cur = arr[i]
    
    return answer