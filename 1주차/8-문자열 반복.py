R = int(input())
for i in range(R):
    P, S = input().split()
    for i in range(len(S)):
        print(S[i] * int(P), end='')
    print()