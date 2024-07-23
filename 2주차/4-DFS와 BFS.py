N,M,V = map(int,input().split())
#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1 # 입력받은 간선을 그래프에 표현
#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()
#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)
#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 
    while queue:
        V = queue.pop(0) #앞에서 부터 빼니까 넓이우선탐색
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)#V와 연결된 노드 차곡차곡 큐로
                visited2[i] = 1
dfs(V)
print()
bfs(V)