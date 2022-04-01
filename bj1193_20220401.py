import sys
n = int(sys.stdin.readline())
maxCount = 1
while n > maxCount:
  n -= maxCount
  maxCount += 1
if maxCount % 2 == 1:
  print("%d/%d"%(maxCount+1-n, n))
else:
  print("%d/%d"%(n, maxCount+1-n))

'''
Question Pattern (ZigZag)
1 : 1/1                                  -> 1
2 : 1/2 , 3 : 2/1                        -> 1 + 2
4 : 3/1 , 5 : 2/2 , 6 : 1/3 (O)          -> 1 + 2 + 3       < 4 : 1/3 , 5 : 2/2 , 6 : 3/1 (X) >
7 : 1/4 , 8 : 2/3 , 9 : 3/2 , 10 : 4/1   -> 1 + 2 + 3 + 4
...
'''