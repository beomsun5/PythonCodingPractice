import sys
word_list = []            # the original list with the given words
tempWord_list = []        # list that contains the words which have the same length
newWord_list = []         # new list which has the right order of the words
result_list = []          # The result
# Get the number of the words
N = int(sys.stdin.readline())
# Get the words
for i in range(N):
  word_list.append(sys.stdin.readline().rstrip())
# Sort the list in order of the word length
wordLenCount = 1
while len(newWord_list) != N:
  for word in word_list:
    if len(word) == wordLenCount:
      tempWord_list.append(word)
  tempWord_list.sort()
  newWord_list.extend(tempWord_list)
  wordLenCount += 1
  tempWord_list.clear()
# Remove the word that repeats
for word in newWord_list:
  if word in result_list:
    continue
  else:
    result_list.append(word)
# Print the result
for word in result_list:
  print(word)