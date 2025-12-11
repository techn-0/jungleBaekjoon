def solution(participant, completion):
    dic = {}
    
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # print(dic)
    for i in completion:
        dic[i] -= 1
    for a, b, in dic.items():
        # print(a, b)
        if b != 0:
            return a
        