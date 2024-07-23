N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

end = arr[0][1] # 첫 번째 회의를 선택하고, 종료 시간을 end_time에 저장
count = 1
for i in range(1, N):
    if end <= arr[i][0]: # 현재 회의의 시작 시간이 이전 회의의 종료 시간 이후일 경우
        count += 1
        end = arr[i][1] # 현재 회의의 종료 시간으로 업데이트
print(count)