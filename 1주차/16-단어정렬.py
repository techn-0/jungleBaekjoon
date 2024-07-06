n = int(input())

words = [str(input()) for i in range(n)]

words = sorted(set(words))
for i in range(1, len(words)):
    for j in range(1, 0, -1):
        if words[j] < words[j - 1]:
            words[j], words[j - 1] = words[j - 1], words[j]

for i in words:
    print(i)
