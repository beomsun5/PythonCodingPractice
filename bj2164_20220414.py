import sys
from collections import deque
# Get the numbers of the card
N = int(sys.stdin.readline())
'''
 Deque : a type of data structure which looks similar to Queue, but this type is able
         to append or pop the component from both the left side and the right side.
'''
d = deque()
for n in range(1, N+1):
  d.append(n)
while 1:
  if len(d) == 1:
    print(d.pop())
    break
  else:
    d.popleft()
    d.append(d.popleft())
  print(d)