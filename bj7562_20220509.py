from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(cur_x, cur_y, goal_x, goal_y):
  d = deque()
  d.append([cur_x, cur_y])
  chessBoard[cur_x][cur_y] = 1
  while d:
    print(d)
    a, b = d.popleft()
    if a == goal_x and b == goal_y:
      print(chessBoard[a][b] - 1)
      return
    for i in range(8):
      newX = a + dx[i]
      newY = b + dy[i]
      if 0 <= newX < l and 0 <= newY < l and chessBoard[newX][newY] == 0:
        d.append([newX, newY])
        chessBoard[newX][newY] = chessBoard[a][b] + 1

t = int(input())
for _ in range(t):
  l = int(input())
  chessBoard = [[0]*l for i in range(l)]
  cur_x, cur_y = map(int, input().split())
  goal_x, goal_y = map(int, input().split())
  bfs(cur_x, cur_y, goal_x, goal_y)

'''
# My solution : By using BFS graph traversal, get the minimum movement of the knight (Did not get the main point of BFS)
import sys
t = int(sys.stdin.readline())

def moveKnight(chessBoard, cur_x, cur_y, goal_x, goal_y, move):
  print(move, cur_x, cur_y, goal_x, goal_y)
  if cur_x == goal_x and cur_y == goal_y:
    print(chessBoard[cur_x][cur_y])
    return
  move_x = [1, 2, 2, 1, -1, -2, -2, -1]
  move_y = [2, 1, -1, -2, -2, -1, 1, 2]
  move += 1
  for i in range(8):
    if 0 <= cur_x + move_x[i] < len(chessBoard[0]) and 0 <= cur_y + move_y[i] < len(chessBoard[0]):
      if chessBoard[cur_x + move_x[i]][cur_y + move_y[i]] == '0':
        new_x = cur_x + move_x[i]
        new_y = cur_y + move_y[i]
        chessBoard[new_x][new_y] = move
        moveKnight(chessBoard, new_x, new_y, goal_x, goal_y, move)
      
for _ in range(t):
  move = 0
  l = int(sys.stdin.readline())
  chessBoard = [['0']*l for i in range(l)]
  cur_x, cur_y = map(int, sys.stdin.readline().split())
  goal_x, goal_y = map(int, sys.stdin.readline().split())
  moveKnight(chessBoard, cur_x, cur_y, goal_x, goal_y, move)
'''