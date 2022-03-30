import sys
from time import time
word = sys.stdin.readline()
timeToCall = 0
for c in word:
  if (65 <= ord(c) <= 67):          # When you choose one among 'ABC'
    timeToCall += 3
  elif (68 <= ord(c) <= 70):        # When you choose one among 'DEF'
    timeToCall += 4
  elif (71 <= ord(c) <= 73):        # When you choose one among 'GHI'
    timeToCall += 5
  elif (74 <= ord(c) <= 76):        # When you choose one among 'JKL'
    timeToCall += 6
  elif (77 <= ord(c) <= 79):        # When you choose one among 'MNO'
    timeToCall += 7
  elif (80 <= ord(c) <= 83):        # When you choose one among 'PQRS'
    timeToCall += 8
  elif (84 <= ord(c) <= 86):        # When you choose one among 'TUV'
    timeToCall += 9
  elif (87 <= ord(c) <= 90):        # When you choose one among 'WXYZ'
    timeToCall += 10
print(timeToCall)
