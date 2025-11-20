time, mine = map(int, input().split())
needTime = int(input())

mine = mine + needTime
if mine >= 60:
    while mine >= 60:
        mine -= 60
        time += 1
if time >= 24:
    time -= 24
print(time, mine)