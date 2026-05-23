def solution(nums):
    answer = 0
    n = len(nums) /2
    pikas = set(nums)
    return min(n, len(pikas))