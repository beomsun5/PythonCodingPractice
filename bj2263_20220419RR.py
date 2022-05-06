# Other Solution
import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

pos = [0]*(n+1)
for i in range(n):
  pos[in_order[i]] = i # Matching and insert the index (position) into the list 'pos'

# 전위 순회
def divide(in_start, in_end, p_start, p_end):

  if(in_start > in_end) or (p_start > p_end):
    return

  parents = post_order[p_end]     # 후위순회에서 부모노드 찾기
  print(parents, end=" ")

  left = pos[parents] - in_start  # 왼쪽인자 갯수
  right = in_end - pos[parents]   # 오른쪽인자 갯수

  divide(in_start, in_start+left-1, p_start, p_start+left-1)  # 왼쪽 노드
  divide(in_end-right+1, in_end, p_end-right, p_end-1)        # 오른쪽 노드

divide(0, n-1, 0, n-1)

''' <My Solution> - 2nd Trial -> Compiling Time Exceeded (== inefficient)
import sys
sys.setrecursionlimit(10**6)  # 파이썬 기본 재귀 깊이 제한 : 1000 -> 1000000으로 세팅해주는 코드
                              # 만약 이 코드를 사용하지 않는다면, 런타임 에러(Recursion Error) 발생

def divTree(tree, po_list):
  if len(tree) == len(po_list):
  # At first, the last element of the inOrder_list is the root of the original tree.
    root = po_list.pop()
  else:
    if len(tree) == 0:
      return
  # Set the root of the given tree
    nodeIdx_list = []
    for node in tree:
      nodeIdx_list.append(po_list.index(node))
    root = po_list[max(nodeIdx_list)]
  if root == None:
    return
  # Divide the tree into 3 parts: root, left subtree, right subtree
  left_subT = tree[:tree.index(root)]
  right_subT = tree[tree.index(root)+1:]
  print(root, end = " ")
  divTree(left_subT, po_list)
  divTree(right_subT, po_list)

n = int(sys.stdin.readline())
inOrder_list = sys.stdin.readline().split()
postOrder_list = sys.stdin.readline().split()
divTree(inOrder_list, postOrder_list)
'''

'''
1. set root
2. divide the inorder list into 3 parts: left subtree, root, right subtree
3. implement the loop of 1 and 2
### The condition to end the loop : 
'''

''' <My Solution> -> Too Much Time for compiling (== inefficient)
import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None
  def preOrder(self, node):
    if node != None:  
      print(node.data, end=" ")
      self.preOrder(node.left)
      self.preOrder(node.right)

def traversal(pNode, node, o_list, checkConnection):
    if node != None:
      if o_list.index(node.data) < o_list.index(pNode.data):
        if pNode.left == None:
          pNode.left = node
          checkConnection = 1
      else:
        if pNode.right == None:
          pNode.right = node
          checkConnection = 1
    return pNode, checkConnection

n = int(sys.stdin.readline())
inOrder_list = sys.stdin.readline().split()
postOrder_list = sys.stdin.readline().split()
node_list = []
root = Node(postOrder_list.pop())
node_list.append(root)
while postOrder_list:
  newNode = Node(postOrder_list.pop())
  checkConnection = 0
  for pN in node_list:
    pN, checkConnection = traversal(pN, newNode, inOrder_list, checkConnection)
    if checkConnection == 1:
      break
  node_list.append(newNode)

bt = BinaryTree()
bt.preOrder(root)
'''