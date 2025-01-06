from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_sizes = {}  # 석유 덩어리의 크기 저장 (덩어리 번호: 크기)
    oil_map = [[-1] * m for _ in range(n)]  # 각 칸의 석유 덩어리 번호 저장
    oil_id = 0  # 석유 덩어리 번호
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동

    # BFS로 석유 덩어리 탐색
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        oil_map[x][y] = oil_id
        size = 0

        while queue:
            cx, cy = queue.popleft()
            size += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    oil_map[nx][ny] = oil_id
                    queue.append((nx, ny))
        return size

    # 각 석유 덩어리 크기 계산
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                oil_sizes[oil_id] = bfs(i, j)
                oil_id += 1

    # 각 열에 대해 석유 덩어리 크기 합산
    max_oil = 0
    for col in range(m):
        seen = set()  # 중복된 석유 덩어리 제거
        total_oil = 0
        for row in range(n):
            oil = oil_map[row][col]
            if oil != -1 and oil not in seen:
                seen.add(oil)
                total_oil += oil_sizes[oil]
        max_oil = max(max_oil, total_oil)

    return max_oil
