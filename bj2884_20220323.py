h, m = map(int, input().split()) # Hour and Minute
if(m < 45): # If the minute of the present time is less than 45
  if(h == 0): # If the hour of the present time is 0
    h = 23
    m += 15
  else:
    h -= 1
    m += 15
else: m -= 45 # If the minute of the present time is more than 45
print(h, m)