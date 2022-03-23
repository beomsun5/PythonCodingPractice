a, b = map(int, input().split())  # The present time (Hour, Minute)
c = int(input())                  # Total Time to cook
if(b + c >= 60):                  # If the sum of b and c equals to or more than 60
  a += int((b+c) / 60)
  b = (b+c) % 60
  if(a > 23): a -= 24             # If a becomes more than 23
else: b += c
print(a, b)