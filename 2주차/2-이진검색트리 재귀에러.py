import sys
input = sys.stdin.readline

arr = []

while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def post(root):
    if root:  # 현재 노드가 None이 아닌 경우만 처리
        if root.left is not None:
            post(root.left)  # 왼쪽 서브트리 방문
        if root.right is not None:
            post(root.right)  # 오른쪽 서브트리 방문
        print(root.key)  # 현재 노드 출력

root = None
for key in arr:
    root = insert(root, key)

post(root)