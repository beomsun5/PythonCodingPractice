import sys
n = int(sys.stdin.readline())
scoreCount = 0                  # Add the score if there are consecutive Os
totalScore = 0                  # Show the total score of the given string
for i in range(n):
  totalScore = 0
  strXO = sys.stdin.readline()
  for ch in strXO:
    if ch == 'O':
      scoreCount += 1
      totalScore += scoreCount
    else:
      scoreCount = 0
  print(totalScore)