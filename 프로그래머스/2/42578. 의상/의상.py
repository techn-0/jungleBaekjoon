def solution(clothes):
    answer = 0
    
    dic = {}
    
    for i in clothes:
        # print(i[1])
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
            
    sum = 1
    for i in dic.values():
        sum *= i + 1
    return sum - 1


# clothes[n][1]은 옷의 종류를 나타냄 같은 종류의 옷은 또 못입음