import sys
a, b = sys.stdin.readline().split()
newA = int(a[2] + a[1] + a[0])
newB = int(b[2] + b[1] + b[0])
print(max(newA, newB))