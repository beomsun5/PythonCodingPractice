import sys
n = int(sys.stdin.readline())
num_list = sys.stdin.readline().split()   # Don't forget to put () after inserting split method
m = max(map(int, num_list))               # map returns object type, so don't use it at the deifinition part
newAvg = 0                                # if you are going to use the list more than one time
for i in map(int, num_list):
  i = i / m * 100                 # New scores for the new average
  newAvg += i
print(newAvg/n)