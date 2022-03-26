import sys
while 1:
  try:
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
  except EOFError:    # If the user ends the program with EOF, this exception is going to be executed.
    break
  except ValueError:  # If the user does not input anything, this exception is going to be executed.
    break             # This program expects to get 2 integers from the user, but if the user just presses the enter key
                      # and terminates the program, ValueError occurs.
