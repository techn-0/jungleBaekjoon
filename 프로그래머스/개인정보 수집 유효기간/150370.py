def solution(today, terms, privacies):
    spl_Today = list(map(int, today.split(".")))
    numToday = ((spl_Today[0] * 12) * 28) + (spl_Today[1] * 28) + spl_Today[2]
    # 날짜를 일로 변환환

    dic_terms = {} # 약관 타입별 만료일을 계산해 딕셔너리로 맹근다
    for i in terms:
        term_type, term_expDay = i.split()
        dic_terms[term_type] = int(term_expDay) * 28

    answer = []

    for i in range(len(privacies)): # 동의한 약관의 수만큼 반복해준다다
        pri_start, pri_type = privacies[i].split()
        pri_start = list(map(int, pri_start.split(".")))
        num_pri_start = ((pri_start[0] *12) * 28) + (pri_start[1] * 28) + pri_start[2]
        # 약관 가입한 날짜를 일 기준으로 컨버팅 해준다다

        exp_day = num_pri_start + dic_terms[pri_type]
        # 타입을 딕셔너리에서 찾아서 만료일을 찾는다

        if numToday>= exp_day: # 만료일이 지난놈을 찾는다다
            answer.append(i + 1)
    return answer