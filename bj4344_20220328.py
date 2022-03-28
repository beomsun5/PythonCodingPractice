import sys
c = int(sys.stdin.readline())
for i in range(c):
  avg = 0                                         # Average of the given scores
  stdNumOvrAvg = 0                                # Student Numbers whose scores are over the average
  stdScoreList = sys.stdin.readline().split()
  tCaseNum = int(stdScoreList.pop(0))             # Exclude the first element which is the number of the cases
  
  # Get the average of the given scores
  for score in map(int, stdScoreList):
    avg += score
  avg /= len(stdScoreList)

  # Get the ratio of the students' number whose score is higher than the average and print it in the percentage format
  for score in map(int, stdScoreList):
    if (score > avg): stdNumOvrAvg += 1
  print("{:.3%}".format( float( stdNumOvrAvg / len(stdScoreList) )))