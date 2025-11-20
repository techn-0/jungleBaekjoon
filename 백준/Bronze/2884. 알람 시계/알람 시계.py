time, mine = map(int, input().split())
# 분이 45 이하일때 시간에서 1을 빼고 분에 60을 더해줘야함
# 분이 45라 시간에서 1을 빼야하는데 시간이 0이라면 23시로 바꿔줘야함

if mine < 45:
    if time == 0:
        time = 23
    else:
        time -= 1
    mine += 60
mine -= 45
print(time, mine)