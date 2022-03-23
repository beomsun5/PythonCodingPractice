a, b, c = map(int, input().split())
if((a==b)&(a==c)&(b==c)): print(10000 + a*1000) # If every number is the same
elif((a==b)|(a==c)|(b==c)):                     # If two of three numbers are the same
  if((a==b)|(a==c)): print(1000 + a*100)
  else: print(1000 + b*100)
else: print(max(a, max(b, c))*100)              # If every number is different from one another
