def solution(A):
    num = set(A)
    visit = set()
    for i in range(len(A)):
        visit.add(A[i])
        if num == visit:
            return i