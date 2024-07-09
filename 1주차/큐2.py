import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([])


for i in range(N):
    commands = sys.stdin.readline().split()
    if commands[0] == 'push':
        q.append(commands[1])
    elif commands[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif commands[0] == 'size':
        print(len(q))
    elif commands[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif commands[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif commands[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])