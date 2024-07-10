n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
l = 0
r = n-1
x = a[n//2]

while l <= r:
    while a[l] < x : l += 1
    while a[r] > x :  l -= 1
    if l <=r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
print(a)