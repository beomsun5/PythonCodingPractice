import sys
n = int(sys.stdin.readline())                 # Test Case Number
groupWordCount = 0                            # Count the number of group Words

# In this 'for' statement, check if the given word is a group word
for i in range(n):
  testWord = sys.stdin.readline().strip()
  pastChars = []                                  # Save the characters which you have already checked in the string
  groupWordOrNot = 1                              # If 1, it is a group word. If 0, it is not a group word.
  for idx in range(len(testWord)):
    if testWord[idx] in pastChars:                # If there is the character which was already checked at the front
      if testWord[idx-1] != testWord[idx]:        # If two characters at the consecutive locations are not the same
        groupWordOrNot = 0                        # IF THE CHARACTER SATISFIES TWO CONDITIONS ABOVE, THIS WORD IS NOT A GROUP WORD.
        break # We don't have to check the other characters, because we just found out this is not a group word.
    else:
      pastChars.append(testWord[idx])             # If this character is first found, put it into the pastChars list
  if groupWordOrNot == 1: groupWordCount += 1     # If there is not any error, this word is a group word, so increment groupWordCount.
print(groupWordCount)