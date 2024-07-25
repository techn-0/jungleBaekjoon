N = int(input())
arr = []
index = []
for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[2], x[1]))

end = arr[0][2] # 첫 번째 회의를 선택, 종료 시간 end 저장
index.append(arr[0][0])
count = 1
for i in range(1, N):
    if end <= arr[i][1]: # 현재 회의의 시작 시간이 이전 회의의 종료 시간 이후일 경우
        count += 1
        end = arr[i][2] # 현재 회의의 종료 시간으로 업데이트
        index.append(arr[i][0])
print(count)
print(index)