import sys
num_list = []
difNumCount = 0     # Variable to get the numbers of the components which are not the same as others
for i in range(10):
  num_list.append(int(sys.stdin.readline())%42) # Add the remainder of the numbers which are divided by 42 to the num_list
for i in range(10):
  for j in range(i+1, 10):
    if(num_list[i] == num_list[j]): num_list[j] = -1 # If there is the same remainder, every repeated remainders become -1, except the original
for num in num_list:
  if(num == -1): continue
  difNumCount += 1
print(difNumCount)