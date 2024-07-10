N = int(input())
words = set()
for _ in range(N):
    words.add(input().strip())
sorted_words = sorted(words, key=lambda word: (len(word), word))
for word in sorted_words:
    print(word)