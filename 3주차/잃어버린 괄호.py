N = str(input())
M = N.split('-')

ans = 0

x = sum(map(int, (M[0].split('+'))))

ans += x

for x in M[1:]:
    x = sum(map(int, (x.split('+'))))
    ans -= x
print(ans)