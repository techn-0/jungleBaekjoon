def plusC(num, count):
    tempNum = (num // 10) + (num % 10)
    newNum = (num % 10) * 10 + (tempNum % 10)
    count += 1
    if newNum == N:
        print(count)
        return
    plusC(newNum, count)
N = int(input())
if N < 10:
    num = N * 10
else:
    num = N
count = 0
plusC(N, count)