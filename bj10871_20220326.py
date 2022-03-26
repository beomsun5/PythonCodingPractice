import sys
n, x = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()    # Using split(), it returns the list type,
                                    #which means the variable that gets the return value of
                                    # split() becomes the list type.
l = []
for i in a:
  if int(i) < x:              # Every factor in the list 'a' is string type, so we have to cast its type into int for the comparison
    l.append(i)               # Add the factor on the list 'l'
print(*l)                     # Print the factors in the list using whitespaces between each factor