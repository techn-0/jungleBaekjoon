n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

# 물건 리스트
for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:   # 물건무계가 더 커서 안들어간다면
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
            # 현재 넣을 물건의 크기만큼 빼고 현재 물건을 넣는이유
            # 이미 물건을 넣은 상태에서 새 물건이 들어갈 공간이 확보되는지 확인하기 위함

print(d[n][k])