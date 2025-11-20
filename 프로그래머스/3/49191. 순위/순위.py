def solution(n, results):
    
    win = [[False] * (n+1) for _ in range(n + 1)]
    
    for a, b in results:
        win[a][b] = True
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if win[i][k] == True and win[k][j]:
                    win[i][j] = True
    answer = 0
    
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if i==j:
                continue
            if win[i][j] == True or win[j][i] == True:
                cnt += 1
                if cnt == n-1:
                    answer +=1
    return answer



# 모든 노드와 연결되어있는 노드를 찾는건가?