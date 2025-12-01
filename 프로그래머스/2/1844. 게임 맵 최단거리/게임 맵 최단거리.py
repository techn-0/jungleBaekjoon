from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 방문 체크 배열
    visited = [[False] * m for _ in range(n)]
    
    # 상하좌우 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 큐 생성 및 시작점 추가
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True  # 시작점 방문 체크
    
    while queue:
        row, col, distance = queue.popleft()
        
        # 목적지 도착 체크
        if row == n-1 and col == m-1:
            return distance
        
        # 4방향 탐색
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            
            # 이동 가능한지 체크
            if (0 <= new_row < n and 0 <= new_col < m and
                maps[new_row][new_col] == 1 and
                not visited[new_row][new_col]):
                
                visited[new_row][new_col] = True  # 방문 체크
                queue.append((new_row, new_col, distance + 1))    # 큐에 추가
    
    return -1