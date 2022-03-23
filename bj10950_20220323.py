t = int(input())                    # Test Case Number
result = []                         # Result list
for i in range(t):
  a, b = map(int, input().split())
  result.append(a+b)       
for i in result: print(i)