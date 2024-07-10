n = int(input())
for i in range(n):
    P, S = input().split()
    for i in S:
        print(i * int(P), end='')
    print()