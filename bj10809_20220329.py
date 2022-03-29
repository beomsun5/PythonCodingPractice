import sys
alphabet_list = []                                        # Alphabet list from A to Z (26 Letters in Total)
word = sys.stdin.readline().rstrip()                      # By using rstrip(), 'word' excludes the EOF(Enter Buffer)
# The default component of the list is -1
for i in range(26):
  alphabet_list.append(-1)
# Have to input the index of each character, so use 'for' statement with range()
for idx in range(len(word)):
  # Substract 97 from specified alphabet letter value is the index of the alphabet (0 ~ 26)
  # ord() converts the character into the original integer value(ASCII CODE VALUE)
  if alphabet_list[ord(word[idx]) - 97] != -1: continue
  else: alphabet_list[ord(word[idx]) - 97] = idx
for c in alphabet_list:
  print(c, end=" ")
print()
