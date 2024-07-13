import sys
input = sys.stdin.readline

class nod:
    def __init__(self,item, left, right):
        self.item = item
        self.left = left
        self.right = right

def pre(nod):
    print(nod.item, end = '')
    if nod.left !='.':
        pre(tree[nod.left])
        #왼쪽꺼부터 재귀로 점점 아래로
    if nod.right !='.':
        pre(tree[nod.right])
        #이제 루트의 오른쪽 자식부터 재귀하며 반복

def mid(nod):
    if nod.left !='.':
        mid(tree[nod.left])
    print(nod.item, end = '')
    if nod.right !='.':
        mid(tree[nod.right])

def post(nod):
    if nod.left !='.':
        post(tree[nod.left])
    
    if nod.right !='.':
        post(tree[nod.right])
    print(nod.item, end = '')

n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

tree = {}

for item, left, right in arr:
    tree[item] = nod(item, left, right)

pre(tree['A'])
print()
mid(tree['A'])
print()
post(tree['A'])
print()