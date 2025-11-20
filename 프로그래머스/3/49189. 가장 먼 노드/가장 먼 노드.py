from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[]for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = [-1] *(n+1)
    distance[1] = 0
    
    q = deque([1])
    
    while q:
        curr = q.popleft()
        for next in graph[curr]:
            if distance[next] == -1:
                distance[next] = distance[curr] + 1
                q.append(next)

    maxDist = max(distance)
    answer = distance.count(maxDist)
    return answer