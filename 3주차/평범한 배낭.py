N, K = map(int, input().split())

zim = [[0,0]]

bag = [[0] * (K + 1)for _ in range(N + 1)]

for i in range(N):
    zim.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = zim[i][0]
        v = zim[i][1]

        # 물건무계가 더 커서 안들어가면 이전물건 넣었을때 최고값
        if j < w:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(bag[i - 1][j], bag[i-1][j-w] + v)
            # 현재 넣을 물건의 크기만큼 빼고 현재 물건을 넣는이유
            # 이미 물건을 넣은 상태에서 새 물건이 들어갈 공간이 확보되는지 확인하기 위함
print(bag[N][K])