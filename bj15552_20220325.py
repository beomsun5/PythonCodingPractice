# sys.stdin.readline() is much faster and allocate less memories than input() does.
import sys

t = int(sys.stdin.readline())
for i in range(t):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)