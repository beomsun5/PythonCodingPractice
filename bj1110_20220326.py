import sys
n = int(sys.stdin.readline())
n_temp = 0          # The total of each digit of n
cycleLength = 0     # The variable to get the length of n's cycle
newNum = n          # The main variable which is going to be compared to n right after each loop

# The condition of this problem is restricting the range of the input from 0 to 99, 2-digit-number
while 1:
  n_temp = int(newNum/10)+newNum%10   # The total of each digit of n
  newNum = (newNum%10)*10 + n_temp%10 
  cycleLength += 1
  if(n == newNum): break
print(cycleLength)