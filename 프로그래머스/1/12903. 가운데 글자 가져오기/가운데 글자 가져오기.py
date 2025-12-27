def solution(s):
    answer = ''
    isOdd = False
    l = len(s)
    mid = (l//2 + 1)-1
    
    if l%2 != 0:
        answer += s[mid]
    else:
        answer += s[mid-1]
        answer += s[mid]
        # mid = l//2
        # mid2 = mid1 + 1
    return answer