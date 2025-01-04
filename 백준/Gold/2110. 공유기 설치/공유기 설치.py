n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))  # 집 위치 정렬

min, max = 1, houses[-1] - houses[0]  #최대 최소 거리
result = 0

def install(dis):
    cnt = 1
    cur = houses[0]

    for i in range(1, n):
        if houses[i] - cur >= dis:
            cnt += 1
            cur = houses[i]
            if cnt >= c:
                return 1
    return 0

while min <= max:
    mid = (min + max) // 2
    if install(mid):
        result = mid
        min = mid + 1
    else:
        max = mid - 1

print(result)