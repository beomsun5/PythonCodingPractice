import sys

def digitNumDif(n):
  digit_list = []
  numDif = 0
  while(n != 0):
    digit_list.append(n%10)
    n //= 10
  # From 1 to 99, every number is the cases we are looking for
  if (len(digit_list) <= 2):                                  
    return 1
  # From 100, each number has more than two differences, so we have to compare them.
  else:                                                       
    numDif = digit_list[0] - digit_list[1]        # Set the difference of the first and second digit of the number
    for i in range(1, len(digit_list)-1):         # and check if other differences is the same as the original value using the loop.
      if numDif == digit_list[i] - digit_list[i+1]: continue
      else: return 0
    return 1

n = int(sys.stdin.readline())
count = 0                                 # Count the number which is the case
for i in range(1, n+1):
  if digitNumDif(i) == 1: count += 1
  else: continue
print(count)