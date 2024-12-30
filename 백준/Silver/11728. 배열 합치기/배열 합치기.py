N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# sumList = A + B
# for i in range(len(sumList) - 1):
#     for j in range(len(sumList) - i - 1):
#         if sumList[j] > sumList[j + 1]:
#             sumList[j], sumList[j + 1] = sumList[j + 1], sumList[j]
sumList = sorted(A + B)

print(*sumList)