T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    asc = sorted(arr)
    top = 0
    result = 1   # 첫 번째 사원 채용
    for i in range(1, len(asc)):
        if asc[i][1] < asc[top][1]: # 현재 사원보다 면접 점수가 낮은 경우
            top = i
            result += 1
    
    print(result)