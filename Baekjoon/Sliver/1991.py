# Sliver 1
# 트리 순회


class Node:
  def __init__ (self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

def preorder(node):
  print(node.item, end="")
  if node.left != ".":
    preorder(tree[node.left]) # node.left를 key 값으로 tree에서 해당하는 값의 노드를 찾고, 다시 재귀호출
  if node.right != ".":
    preorder(tree[node.right]) # node.right를 key 값으로 tree에서 해당하는 값의 노드를 찾고, 다시 재귀호출

def inorder(node):
  if node.left != ".":
    inorder(tree[node.left])
  print(node.item, end="")
  if node.right != ".":
    inorder(tree[node.right])

def postorder(node):
  if node.left != ".":
    postorder(tree[node.left])
  if node.right != ".":
    postorder(tree[node.right])
  print(node.item, end="")

N = int(input())
# 포인트! 트리를 Dictionary로 선언해준다!
# key값으로 value를 찾아서 넘겨줘야 트리가 연결될 수 있음
tree = {}
for i in range(N):
  node, leftNode, rightNode = input().split()
  # key: 노드의 값 value: 해당 노드 값을 갖는 Node 클래스의 인스턴스
  tree[node] = Node(node, leftNode, rightNode)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
