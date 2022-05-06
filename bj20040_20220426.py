# Union-Find 함수 이용 문제
# 답안
import sys
n, m = map(int, sys.stdin.readline().split())
parents = [i for i in range(n)]
endgame = 0

def find(x):
  if x == parents[x]:
    return x
  else:
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y, idx):
  global endgame
  # x, y : x, y의 값
  x = find(x)
  y = find(y)
  # x, y : x, y의 루트
  if x != y:  # x, y의 루트가 다를 때,
    parents[max(x, y)] = min(x, y)
  # x와 y의 root가 같을 때,
  elif endgame == 0:
    endgame = idx

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  union(a, b, i + 1)
  #print(parents, endgame)
print(endgame)

'''
root_list = [i for i in range(n)]
rank_list = [0]*n # Optimizing Union Function -> Union-by-Height(Rank)
def find(i):
  if root_list[i] == i:
    return root_list[i]
  else:
    # The simplest Find Function
    # return find(root_list[i])
    # Optimized Find Function
    root_list[i] = find(root_list[i])
    return root_list[i]

def union(i, j):
  i = find(i)
  j = find(j)
  if i == j: # If the roots of i and j are the same, no need implementing union
    return
  # Always the tree whose height(rank) is taller becomes the root of the tree whose height is smaller.
  if rank_list[i] < rank_list[j]:
    root_list[i] = j
  elif rank_list[i] > rank_list[j]:
    root_list[j] = i
  else: # If the roots are different, but the rank is the same
    root_list[j] = i
    rank_list[i] += 1
    # Put them together and increment the rank of the root
  
  # The simplest Union Function
  i = find(i)
  j = find(j)
  root_list[j] = i
'''
  
'''
# Fail to compile at Baekjoon website
import sys
n, m = map(int, sys.stdin.readline().split())
point_list = [0]*n      # List for storing the points
line_list = []          # List for storing the lines. Each of them has two points at the end
selected_list = []      # List for the given lines
for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  point_list[x] += 1
  point_list[y] += 1
  # There are no starting point and ending point, so store two version of one line.
  line_list.append((x, y))
  line_list.append((y, x))
# 1st condition for the element of set C : each point has to be reached more than twice
for i in range(m):
  if point_list[i] >= 2: selected_list.append(i)
lineCount = 0
CycleDone = None
# 2nd condition for the element of set C : among more than twice selected points, the lines have to make the cycle
#                                          Cycle : Line numbers == selected point numbers
for i in range(len(selected_list)):
  selected_points = None
  if i == len(selected_list)-1:
    selected_points = (selected_list[i], selected_list[0])
  else:
    selected_points = (selected_list[i], selected_list[i+1])
  for j in range(0, len(line_list), 2):
    if selected_points == line_list[j] or selected_points == line_list[j+1]:
      lineCount += 1
      CycleDone = j//2+1
if lineCount == len(selected_list):
  print(CycleDone)
else:
  print(0)
'''