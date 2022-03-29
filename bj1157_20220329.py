import sys
# It does not matter if the letters which consist of the word are uppercase or lowercase.
# However, we have to print the uppercase letter, make all letters uppercase.
word = sys.stdin.readline().strip().upper()
letter_list = []                              # list which contains the letters of the word
letterCount = []                              # list which contains how many times the specific word is used
maxLettersCount = 0                           # Count the letters which have been used the most at the given word
stdLetter = ""                                # Standard Letter to compare the 
for c in word:
  if c != stdLetter:
    if c not in letter_list:
      letter_list.append(c)
      letterCount.append(1)
    else:
      letterCount[letter_list.index(c)] += 1  
  else:
    letterCount[letter_list.index(c)] += 1
  stdLetter = c
for i in range(len(letter_list)):
  if (letterCount[i] == max(letterCount) & max(letterCount) > 1): maxLettersCount += 1
if maxLettersCount >= 2: print("?")
else: print(letter_list[letterCount.index(max(letterCount))])