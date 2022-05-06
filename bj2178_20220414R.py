# Maze -> Review the code and understand the flow of the codes and keep it in mind.
# This method is using BFS (Breadth-First Search) utilizing queue.
n, m = map(int, input().split())
s = []
queue = []
# Right, Left, Down, Up
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# Make the input managable converting its type from string to list. (Able to access to each character)
# If you cast the type of the string into the list, you can change the character of the string, because its type is changed into the list.
for i in range(n):
  s.append(list(input()))
# (x, y) index of current location
# In this queue, there will be some coordinates which is adjacent to the present location.
queue = [[0, 0]]
# Always the starting point of the maze contains '1'
s[0][0] = 1
# If there is any coordinate in the queue, this loop is executed.
while queue:
  # Pop the first component of the queue (x, y) and store each value into a, b
  a, b = queue[0][0], queue[0][1]
  del queue[0]
  # It is available to get to the next location with 4 directions.
  # Check the location of each direction and choose the ones which satisfy the range of the maze
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    # If either x or y does not exist within the range of the maze, that is not appropriate coordinate for this maze.
    # Therefore, that coordinate should be excluded from being appended into the queue.
    if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
      queue.append([x, y])
      s[x][y] = s[a][b] + 1
print(s[n-1][m-1])