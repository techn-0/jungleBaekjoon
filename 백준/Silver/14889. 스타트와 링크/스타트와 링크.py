N = int(input())  # 사람 수
S = [list(map(int, input().split())) for _ in range(N)]  # 능력치 배열

min_diff = float('inf')  # 최소 능력치 차이를 저장할 변수
visited = [False] * N  # 방문 여부를 저장하는 리스트

def calculate_ability(team):
    ability = 0
    for i in team:
        for j in team:
            if i != j:
                ability += S[i][j]
    return ability

def backtrack(idx, count):
    global min_diff
    
    # N/2명을 선택한 경우, 팀을 나누고 능력치 계산
    if count == N // 2:
        start_team = []
        link_team = []
        
        for i in range(N):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)
        
        # 두 팀의 능력치 계산
        start_ability = calculate_ability(start_team)
        link_ability = calculate_ability(link_team)
        
        # 능력치 차이의 최소값 갱신
        min_diff = min(min_diff, abs(start_ability - link_ability))
        return
    
    # 재귀적으로 N/2명을 선택하는 과정
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True  # i번 사람을 선택
            backtrack(i + 1, count + 1)  # 다음 사람을 선택
            visited[i] = False  # 선택 해제

# 백트래킹 시작
backtrack(0, 0)

# 결과 출력
print(min_diff)
