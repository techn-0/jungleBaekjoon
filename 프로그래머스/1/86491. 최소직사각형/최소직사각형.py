import heapq

def solution(sizes):
    n = len(sizes)
    
    for i in range(n):
        w = sizes[i][0]
        h = sizes[i][1]
        if w < h:
            sizes[i][0] = h
            sizes[i][1] = w
    a = []
    b = []
    for w ,h  in sizes:
        a.append(w)
        b.append(h)
    w = max(a)
    h = max(b)

    return w*h