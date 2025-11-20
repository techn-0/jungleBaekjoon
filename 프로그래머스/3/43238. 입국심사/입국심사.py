def solution(n, times):
    
    def countPeople(mid):
        total = 0
        for t in times:
            total += mid//t
        return total
    
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        if countPeople(mid) >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
