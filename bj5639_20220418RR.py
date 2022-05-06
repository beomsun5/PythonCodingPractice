# Copy of the code from other developer
import sys
sys.setrecursionlimit(10**6)  # 파이썬 기본 재귀 깊이 제한 : 1000 -> 1000000으로 세팅해주는 코드
                              # 만약 이 코드를 사용하지 않는다면, 런타임 에러(Recursion Error) 발생

num_list = []
while 1:
  try:
    num = int(sys.stdin.readline())
    num_list.append(num)
  except:
    break
  
def postOrder(left, right):
  if left > right:
    return
  mid = right + 1       # 분할 기준
  for i in range(left+1, right+1):
    # 해당 원소가 현재 노트보다 크다면 그 전까지는 왼쪽 서브 트리.
    # 해당 원소 이후는 오른쪽 서브 트리이다.
    if num_list[left] < num_list[i]:
      mid = i
      break
  postOrder(left+1, mid-1)
  postOrder(mid, right)
  print(num_list[left])

postOrder(0, len(num_list)-1)

# If the tree size is given, this can be the right answer.
# However, the question does not set the size of the tree, so we have to consider this condition.
'''
import sys

class Node:
  def __init__(self, data):
    self.data = data        # Node Data
    self.left = None        # Room for the link connected to the left subtree
    self.right = None      # Room for the link connected to the right subtree
  def dataInAndTraversal(self, node):
    if node.data < self.data:
      if self.left != None:
        self.left.dataInAndTraversal(node)
      else:
        self.left = node
    else:
      if self.right != None:
        self.right.dataInAndTraversal(node)
      else:
        self.right = node

class BinarySearchTree:
  def __init__(self, node):
    self.root = node
  def postOrder(self, node):
    if node != None:
      self.postOrder(node.left)
      self.postOrder(node.right)
      print(node.data)

rootNode = None
newNode_list = []
for i in range(9):
  newNode = Node(int(sys.stdin.readline()))
  newNode_list.append(newNode)
  if i == 0:
    bst = BinarySearchTree(newNode)
    rootNode = newNode
  else:
    rootNode.dataInAndTraversal(newNode)
bst.postOrder(bst.root)
'''