num = int(input())

f = [list(map(int, input().split())) for _ in range(num)]
f.sort()

total = 0
end_of_world = (3, 1)  # 3월 1일부터 시작
last_flower_end = (0, 0)

i = 0
while i < num and end_of_world <= (11, 30):
    max_end = (0, 0)
    while i < num:
        s_month, s_day, e_month, e_day = f[i]
        if (s_month, s_day) > end_of_world:  # 꽃이 현재 범위 밖이면 종료
            break
        if max_end < (e_month, e_day):
            max_end = (e_month, e_day)  # 더 긴 꽃의 종료일 갱신
        i += 1

    if max_end == (0, 0):  # 더 이상 선택할 꽃이 없으면 실패
        break

    end_of_world = max_end  # 현재 범위 확장
    total += 1  # 사용한 꽃의 수 증가

if end_of_world > (11, 30):
    print(total)
else:
    print(0)
