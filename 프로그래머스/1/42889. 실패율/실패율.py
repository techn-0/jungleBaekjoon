def solution(N, stages):
    answer = []
    fails ={}
    totalPlayers = len(stages)

    for i in range(1, N + 1):
        failPlayer = stages.count(i)

        if failPlayer > 0:
            failPer = failPlayer / totalPlayers
        else:
            failPer = 0

        fails[i] = failPer

        totalPlayers -= failPlayer
    
    answer = sorted(fails, key=lambda x: (-fails[x], x))

    return answer