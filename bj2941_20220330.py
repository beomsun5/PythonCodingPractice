import sys
word = sys.stdin.readline().strip()
croAlphabet = ["c-", "c=", "dz=", "d-", "lj", "nj", "s=", "z="]
for ca in croAlphabet:
  word = word.replace(ca, "1")  # Condsider any element of the croAlphabet list as one character.
print(len(word))