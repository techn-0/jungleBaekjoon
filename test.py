n = int(input())
days = list(map(int, input().split()))

days.sort(reverse=True) # 오래 걸리는것 먼저 심어야 효율적이겠지?
max_days = 0

for i in range(n):
    max_days = max(max_days, i + 1 + days[i])

print(max_days + 1) # 다 자라고 이장님 초대해야 하니 1 더해줘야지지