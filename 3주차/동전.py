import sys

input = sys.stdin.readline

t = int(input())    # 몇번 할건지
for _ in range(t):
    n = int(input())    # 동전 가지수
    coins = list(map(int, input().split())) # 동전 금액(오름차순)
    m = int(input())    # 만들어야 할 금액

    # memoization을 위한 리스트 선언
    d = [0] * (m + 1)   #0원부터 m원까지니 M + 1
    d[0] = 1   # 0원을 만드는 경우는 동전을 0개 쓰는 경우니까 1로 미리 설정

    for coin in coins:
        for i in range(m + 1):
            # a_(i-k) 를 만드는 방법이 존재한다면 
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
            if i >= coin:
                d[i] += d[i - coin]

    print(d[m])