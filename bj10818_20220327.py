import sys
n = int(sys.stdin.readline())
num_list = sys.stdin.readline().split()   # By using split(), get the integers at one line as a string,
                                          # and convert them into a list
print(min(map(int, num_list)), end=" ")   # num_list is the list whose components are the string,
print(max(map(int, num_list)))            # so by using map(), change them into the integers and put them into min() and max()