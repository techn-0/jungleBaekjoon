def solution(n):
    answer = []
    text = list(str(n))
    text.reverse()
    for i in text:
        answer.append(int(i))
    return answer