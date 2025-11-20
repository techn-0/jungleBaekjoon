diceA, diceB, diceC = map(int, input().split())
money = 0

if diceA == diceB == diceC:
    money = 10000 + diceA * 1000
elif diceA == diceB  or diceA == diceC:
    same = diceA
    money = 1000 + same * 100
elif diceB == diceC:
    same = diceB
    money = 1000 + same * 100
else:
    money = max(diceA, diceB, diceC) * 100
print(money)
