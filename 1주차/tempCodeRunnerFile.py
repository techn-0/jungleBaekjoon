def iostr():
    s = input()
    for i in range(0, len(s)):
        for j in range(len(s)):
            print(s[i], end='')

n = int(input())
for i in range(n):
    iostr()
    print()