N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# A를 딕셔너리로 변환
A_dict = {}
for num in A:
    A_dict[num] = True

# B의 각 요소에 대해 A_dict에서 검색
for num in B:
    if num in A_dict:
        print(1)
    else:
        print(0)
