import sys
input = sys.stdin.readline

class node:
    def __init__(self, item, L, R):
        self.item = item
        self.L = L
        self.R = R

def pre(node):
    print(node.item, end = '')
    if node.L != '.':
        pre(tree[node.L])
    if node.R != '.':
        pre(tree[node.R])

def mid(node):
    if node.L != '.':
        mid(tree[node.L])
    print(node.item, end = '')
    if node.R != '.':
        mid(tree[node.R])

def post(node):
    if node.L != '.':
        post(tree[node.L])
    if node.R != '.':
        post(tree[node.R])
    print(node.item, end = '')

N = int(input())
arr = []

for i in range(N):
    arr.append(input().split())

tree = {}

for item, L, R in arr:
    tree[item] = node(item, L, R)

pre(tree['A'])
print()
mid(tree['A'])
print()
post(tree['A'])