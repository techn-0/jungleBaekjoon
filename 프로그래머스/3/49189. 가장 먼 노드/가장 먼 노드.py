from collections import deque

def solution(n, edge):
    graph = [[]for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = [-1] * (n+1)
    distance[1] = 0
    
    q = deque([1])
    
    while q:
        curr = q.popleft()
        for nxt in graph[curr]:
            if distance[nxt] == -1:
                distance[nxt] = distance[curr] + 1
                q.append(nxt)
    maxDistance = max(distance)
    answer = distance.count(maxDistance)
    
    return answer