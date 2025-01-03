n = int(input())
days = list(map(int, input().split()))

days.sort(reverse=True)

max_days = 0

for i in range(n):
    max_days = max(max_days, i + 1 + days[i])

print(max_days + 1) 