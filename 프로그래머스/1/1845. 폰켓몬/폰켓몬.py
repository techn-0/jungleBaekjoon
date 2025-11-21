def solution(nums):
    answer = 0
    n = len(nums)
    
    # 포켓몬의 종류:마리수 저장 딕셔너리 만들자
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    # ----------------
    kinds = len(dic)
    limit = n/2
    answer = min(kinds, limit)
    
    return answer