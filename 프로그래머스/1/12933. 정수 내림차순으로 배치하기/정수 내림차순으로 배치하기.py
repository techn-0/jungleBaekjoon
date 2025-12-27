def solution(n):
    text = ""
    s = str(n)
    s = list(s)
    s.sort(reverse = True)
    for i in s:
        text += i
    return int(text)