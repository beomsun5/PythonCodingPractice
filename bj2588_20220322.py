# Without using the loop
"""
n1 = int(input())
n2 = int(input())
total = 0
total += n1*(int(n2%10))
print(n1*(int(n2%10)))
n2 /= 10
total += n1*(int(n2%10))*10
print(n1*(int(n2%10)))
n2 /= 10
total += n1*(int(n2%10))*100
print(n1*(int(n2%10)))
print(total)
"""
# Using the loop
n1 = int(input())
n2 = int(input())
total = 0
digitMatch = 10
for i in range(3):
  print(n1*(int(n2%10)))
  total += n1*(int(n2%10))*digitMatch
  n2 /= 10
  digitMatch *= 10
print(total)