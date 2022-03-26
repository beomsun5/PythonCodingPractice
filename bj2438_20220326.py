#bj2438
'''
import sys
n = int(sys.stdin.readline())
for i in range(n):
  for j in range(i+1):
    print("*", end="") # This is how to print without using newline
  print()
'''
#bj2439
import sys
n = int(sys.stdin.readline())
for i in range(n):
  for k in range(n-i-1):
    print(" ", end="")
  for j in range(i+1):
    print("*", end="") # This is how to print without using newline
  print()