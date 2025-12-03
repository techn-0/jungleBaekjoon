def solution(participant, completion):
    answer = ''
    
    cnt = {}
    
    for i in participant:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    for i in completion:
        cnt[i] -= 1
    
    for k, v in cnt.items():
        if v != 0:
            return k
    return answer

# participant: 참여선수 이름
# completion: 완주 선수 이름
# answer: 완주 못한 선수 이름
# 동명이인 처리해야함