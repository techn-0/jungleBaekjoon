def iostr():
    m, s = input().split()
    for i in range(0, len(s)):
        for j in range(int(m)):
            print(s[i], end='')
    print()

n = int(input())
for i in range(n):
    iostr()
