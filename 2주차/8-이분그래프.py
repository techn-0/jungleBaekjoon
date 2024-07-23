import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, visited, graph, group):
    visited[start] = group

    for i in graph[start]:
        if visited[i] == 0:
            result = dfs(i, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[i] == group:
                return False
    return True

k = int(input())

for i in range(k):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    
    # 간선의 노드를 입력받아 리스트에 저장하는데 부모를 모름으로 서로 다 해줌
    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    #V의 개수만큼 노드 검사를 진행
    for i in range(1, V+1):
        if visited[i] == 0 :
            result = (dfs(i, visited, graph, 1))
            if not result:
                break
    if result:
        print('YES')
    else:
        print('NO')