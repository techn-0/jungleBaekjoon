N = int(input())
words = set()  # 집합을 사용하여 중복 단어를 제거합니다.

for _ in range(N):
    words.add(input().strip())  # 단어를 입력받아 집합에 추가합니다.

# 중복이 제거된 단어들을 리스트로 변환한 후 정렬합니다.
sorted_words = sorted(words, key=lambda word: (len(word), word))

# 정렬된 단어들을 출력합니다.
for word in sorted_words:
    print(word)
