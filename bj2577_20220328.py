import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
result = a * b * c
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Numbers from 0 to 9
while (result != 0):
  num[result%10] += 1
  result = int(result/10)
for i in num:
  print(i)