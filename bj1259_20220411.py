import sys

while 1:
  n = sys.stdin.readline().rstrip()
  if n == '0':
    break
  pelindromOrNot = 1
  for idx in range((len(n)//2)+1):
    if n[idx] == n[len(n)-1-idx]:
      continue
    else:
      pelindromOrNot = 0
      break
  if pelindromOrNot == 1:
    print("yes")
  else:
    print("no")
