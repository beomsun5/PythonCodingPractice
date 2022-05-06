# Other solution (Success) -> using graph adjacency matrix
import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for i in range(n+1)]
dfs_visit = [0] * n
bfs_visit = [0] * n

for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x][y] = graph[y][x] = 1

# The priciple of DFS : Once you choose the starting vertex, you have to go through all leaves of the root.
#                       Each leaf has their leaves, so until you get to the end, dfs function should be implemented
#                       with the other leaves of the root.
def dfs(v):
  print(v, end = " ")
  dfs_visit[v-1] = 1
  for i in range(1, n+1):
    if dfs_visit[i-1] == 0 and graph[v][i] == 1:
      # Access the leaves by recursion
      dfs(i)

# The priciple of BFS : Once you choose the starting vertex, you have to go through all leaves of the root.
#                       After you get to the all siblings of the leaves at the specific level,
#                       you can traverse the leaves on the next level.
def bfs(v):
  d = deque()
  d.append(v)
  bfs_visit[v-1] = 1
  while d:
    v = d.popleft()
    print(v, end = " ")
    for i in range(1, n+1):
      if bfs_visit[i-1] == 0 and graph[v][i] == 1:
        d.append(i)
        # Once you push a vertex into the queue, that means you have visited the vertex.
        # Therefore, you should make the pushed vertices visited.
        bfs_visit[i-1] = 1

dfs(v)
print()
bfs(v)

# My solution : Failed
'''
import sys
# Expanding the recursion limit (Normally set it to 10^6)
sys.setrecursionlimit(10**6)
# n : number of vertices, m : number of edges, v : the starting vertex
n, m, v = map(int, sys.stdin.readline().split())
stack = []
queue = []
# Graph for DFS and BFS (storing the edges)
gForDFS = []
gForBFS = []
# 0 : not passed vertex, 1 : passed vertex
passedForDFS = [0]*n
passedForBFS = [0]*n

for _ in range(m):
  v1, v2 = map(int, sys.stdin.readline().split())
  gForDFS.append([v1, v2])
  gForBFS.append([v1, v2])

def dfs(v):
  print(v, end=" ")
  passedForDFS[v-1] = 1
  nextV = []  # list for the vertices adjacent to the current vertex
  # Get the adjacent vertices from the edges
  for vtx in gForDFS:
    if v in vtx:
      vtx.remove(v)
      nextV.append(vtx.pop())
  # To pop the least number if there are more than 2 adjacent vertices, sort the list in the reversed order.
  nextV.sort(reverse=True)
  for i in nextV:
    # There could be the situation that both the previous vertex and the current one are linked to the same vertex.
    # This means a vertex could be stored in the stack at the same time, ex) [4, 3, 4]
    # To prevent this problem, we have to remove one of the repeated elements which is at the bottom.
    if i in stack:
      stack.remove(i)
    # Among the adjacent vertices, only the vertices which has not been selected should be pushed into the stack.
    if passedForDFS[i-1] == 0:
      stack.append(i)
  # If the stack is empty, end the function
  if not stack:
    print()
    return
  # If there is any element in the stack, pop it and implement dfs function.
  else:
    dfs(stack.pop())

# bfs function is similar to the dfs function. The difference between them is using the different data structure.
def bfs(v):
  print(v, end=" ")
  passedForBFS[v-1] = 1
  nextV = []
  for vtx in gForBFS:
    if v in vtx:
      vtx.remove(v)
      nextV.append(vtx.pop())
  nextV.sort()
  for i in nextV:
    if i in queue:
      queue.remove(i)
    if passedForBFS[i-1] == 0:
      queue.append(i)
  if not queue:
    return
  else:
    bfs(queue.pop(0))

dfs(v)
bfs(v)
'''