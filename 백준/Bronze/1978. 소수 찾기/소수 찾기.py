n = int(input())
arr = input().split()
count = 0
for i in arr:
    prim = True
    num = int(i)
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                prim = False
                break
        if prim == True:
            count += 1
print(count)