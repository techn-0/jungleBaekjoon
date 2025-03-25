today = input()
toDay = list(map(int, today.split(".")))
numToday = ((toDay[0] * 12) * 28) + (toDay[1] * 28) + toDay[2]
print(numToday)