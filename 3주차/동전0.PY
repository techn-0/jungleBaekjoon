N, K = map(int, input().split())

#동전의 종류를 N번 입력받아 저장
coin = []
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True) #내림차순 정렬

count = 0
#가치가 큰 동전부터 K를 나누고 나머지를 다시K로
for i in coin:
    if K >= i:
        count += K // i
        K %= i #현재 coin으로 나누고난 나머지로 다음 연산 진행
        if K <= 0:
            break
print(count)