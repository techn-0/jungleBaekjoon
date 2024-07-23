import sys
import heapq 
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M+1):
    a, b , c = map(int, input(). split())
    graph[a].append([b, c])

start, end = map(int, input().split())

costs = [1e9 for _ in range(N + 1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])

while heap:
    1