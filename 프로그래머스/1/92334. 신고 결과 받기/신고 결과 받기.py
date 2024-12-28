def solution(id_list, report, k):
    result = [0] * len(id_list) # 일단 result 를 유저 수만큼 크기를가진 리스트로 선언해줌

    report = list(set(report)) # 중복 신고 제거

    reports = {}
    # 신고 내역 딕셔너리를만들건데 신고당한유저가 키값이고 신고한 유저를 벨류로 잡으면 정지된 유저를 신고한 사람에게 문자를 보내기 편할거야

    for i in report:
        Rer, Red = i.split()
        if Red not in reports: # 리폿당한 유저가 딕셔너리에 없음 빈 리스트 추가
            reports[Red] = []
        reports[Red].append(Rer) # 신고당한 사람 딕셔너리에 신고한 사람을 벨류로 넣어줌

    die = [] # 처형할 유저 리스트

    for user, N in reports.items(): # k번 이상 신고당한 유저 선별
        if len(N) >= k:
            die.append(user)

    mail = [0] * len(id_list) # 유저별 알림 발송 횟수 리스트 맹그러둠
    
    for dieU in die:
        for Rer in reports[dieU]:
            mail[id_list.index(Rer)] += 1  # 신고자를 mail 리스트에 반영

    answer = mail  # 최종 메일 발송 횟수 리스트를 answer에 담기
    return answer