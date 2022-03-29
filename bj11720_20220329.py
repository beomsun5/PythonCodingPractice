import sys
strlen = int(sys.stdin.readline())    # Get the length of the string
allNum = sys.stdin.readline()         # Get the value as string type
total = 0
for i in range(strlen):
  total += int(allNum[i])             # By accessing each character of the string and converting it into int, get the total
print(total)