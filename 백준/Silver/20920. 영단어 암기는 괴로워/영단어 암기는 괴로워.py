from collections import Counter

N, M = map(int, input().split())
words = []
for _ in range(N):
    word = input()
    if len(word) >= M:
        words.append(word)

cnt = Counter(words)

wordsBoock = sorted(cnt.keys(), key=lambda x: (-cnt[x], -len(x), x))

for i in wordsBoock:
    print(i)