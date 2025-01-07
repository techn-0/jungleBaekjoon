from collections import deque
def solution(A, K):
    if not A:
        return A
    q = deque(A)
    K = K % len(A)
    for i in range(K):
        temp = q.pop()
        q.appendleft(temp)
    return list(q)