import sys
# The structure of each node (Using Class)
class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right
# This is Binary Tree Class which is going to be used to connect each nodes into the binary tree structure
class BinaryTree:
  def __init__(self):
    self.root = None
  # Traverse the nodes in PreOrder way
  def preOrderT(self, n):
    if n != None: 
      print(n.data, end="")
      if n.left != '.':
        self.preOrderT(n.left)
      if n.right != '.':
        self.preOrderT(n.right)
  # Traverse the nodes in Inorder way
  def inOrderT(self, n):
    if n != None:
      if n.left != '.':
        self.inOrderT(n.left)
      print(n.data, end="")
      if n.right != '.':
        self.inOrderT(n.right)
  # Traverse the nodes in Postorder way
  def postOrderT(self, n):
    if n != None:
      if n.left != '.':
        self.postOrderT(n.left)
      if n.right != '.':
        self.postOrderT(n.right)
      print(n.data, end="")

# Get the number of the nodes
node_num = int(sys.stdin.readline())
# With respect to each node, at any time the node information is given, every node is going to be connected like the binary tree
# which is shown at the top of the question.
node_list = []
# bt : the instance of the BinaryTree class (Role : make every node like the binary tree and implement the 3 ways of traversal)
bt = BinaryTree()
# Get the nodes and convert them into the binary tree
for n in range(node_num):
  data, left, right = sys.stdin.readline().split()
  newNode = Node(data, left, right)
  node_list.append(newNode)
  if n == 0:
    bt.root = node_list[0]
  else:
    # Left and Right of the nodes are the places for storing the address of the pointing node.
    # Therefore, if the data of the node and either the character on the left or right are identical,
    # Change the value of the left or right into the address of the node. 
    for i in range(n):
      if node_list[i].left == node_list[n].data:
        node_list[i].left = node_list[n]
      elif node_list[i].right == node_list[n].data:
        node_list[i].right = node_list[n]

bt.preOrderT(bt.root)
print()
bt.inOrderT(bt.root)
print()
bt.postOrderT(bt.root)