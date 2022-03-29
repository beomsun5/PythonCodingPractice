import sys
t = int(sys.stdin.readline())
for i in range(t):
  reps, word = sys.stdin.readline().split() # reps : repitition for each character, word : given word
  newWord = ""                              # newWord : the result
  for ch in word:
    for i in range(int(reps)):
      newWord += ch                         # Ex) "My" + "String" == "MyString"
  print(newWord)