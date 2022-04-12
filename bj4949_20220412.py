import sys

while 1:
  s = sys.stdin.readline().rstrip()
  # End the program if the given string is "."
  if s == ".": break
  # The stack which would contain parentheses or brackets
  openCloseMarks = []
  # Check whether the remaining marks have their own pair. If yes, 1. Unless, 0.
  tempBool = 1
  for l in s:
    # Push the letter if it is either "(" or "["
    if l == "(" or l == "[":
      openCloseMarks.append(l)
    # If the letter is ")"
    elif l == ")":
      # If the stack is empty or the last mark is "[" -> Error
      if not openCloseMarks or openCloseMarks[-1] == "[":
        tempBool = 0
      # If there is an opening parenthesis at the top of the stack, pop it.
      elif openCloseMarks[-1] == "(":
        openCloseMarks.pop()
    # If the letter is "]"
    elif l == "]":
      # If the stack is empty or the last mark is "(" -> Error
      if not openCloseMarks or openCloseMarks[-1] == "(":
        tempBool = 0
      # If there is an opening bracket at the top of the stack, pop it.
      elif openCloseMarks[-1] == "[":
        openCloseMarks.pop()
  # If the stack is empty and there is no error with the pairing, print "yes"
  if not openCloseMarks and tempBool == 1:
    print("yes")
  else:
    print("no")