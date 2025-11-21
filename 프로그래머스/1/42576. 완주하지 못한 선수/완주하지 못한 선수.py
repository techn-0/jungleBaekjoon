def solution(participant, completion):
    answer = ''
    
    count = {}
    for p in participant:
        if p not in count:
            count[p] = 1
        else: count[p] += 1
    
    for c in completion:
        count[c] -= 1
    
    for name, cnt in count.items():
        if cnt != 0:
            return name
            
    
    

    return answer

# participant: 참여선수 이름
# completion: 완주 선수 이름
# answer: 완주 못한 선수 이름
# 동명이인 처리해야함