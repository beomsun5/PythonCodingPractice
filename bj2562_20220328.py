import sys
num_list = []
for i in range(9):
  num_list.append(int(sys.stdin.readline()))
print(max(num_list))
print(num_list.index(max(num_list))+1)    # The user wants to know when the maximum is inputted, not the index
                                          # Therefore, add 1 after returning index of the component