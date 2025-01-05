def solution(today, terms, privacies):
    spl_Today = list(map(int, today.split(".")))
    numToday = ((spl_Today[0] * 12) * 28) + (spl_Today[1] * 28) + spl_Today[2] # 날짜를 일로 변환환

    dic_terms = {}
    for i in terms:
        term_type, term_expDay = i.split()
        dic_terms[term_type] = int(term_expDay) * 28

    answer = []


    for i in range(len(privacies)):
        pri_start, pri_type = privacies[i].split()
        pri_start = list(map(int, pri_start.split(".")))
        num_pri_start = ((pri_start[0] *12) * 28) + (pri_start[1] * 28) + pri_start[2]

        exp_day = num_pri_start + dic_terms[pri_type]

        if numToday>= exp_day:
            answer.append(i + 1)
    return answer