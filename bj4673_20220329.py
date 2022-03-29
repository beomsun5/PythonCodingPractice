'''
If you tried to solve this problem by making the list including 10000 integers and retrieve the self numbers of the list,
it may cause a great deal of running time so that the compiler cannot afford it.

To simply solve this problem, you have to use the index of the list(array) with the boolean type or using 0 and 1
to clarify whether the specified number is the self number or not.
'''
def d(n):                     # Function to make the number which is not the self number
  allDigitNumSum = n
  while(n != 0):
    allDigitNumSum += n % 10
    n = int(n / 10)
  return allDigitNumSum

num_list = []                 # If a number is a self number, it contains 0. If not, 1.
for i in range(10001):
  num_list.append(0)
for i in range(1, 10001):
  if d(i) <= 10000:
    num_list[d(i)] = 1

for i in range(1, 10001):
  if num_list[i] == 0: print(i)
  else: continue              # Skip the turn if the number is not a self number.