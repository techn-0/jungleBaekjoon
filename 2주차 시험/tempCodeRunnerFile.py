import sys
input = sys.stdin.readline
n = int(input())
apart = []
for i in range(n):
    apart.append(list(map(int,input().split())))

mx = [0,0,1,-1]
my = [1,-1,0,0]

def dfs(x,y):
    global home
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if apart[x][y] == 1:
        home += 1
        apart[x][y] = 0
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            dfs(nx, ny)


home = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(home)
            result+=1
            home = 0