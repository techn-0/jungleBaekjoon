import heapq

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

total_sum= 0

while len(card) > 1:
    c1 = heapq.heappop(card)
    c2 = heapq.heappop(card)

    sum = c1 + c2
    total_sum += sum

    heapq.heappush(card,sum)

print(total_sum)