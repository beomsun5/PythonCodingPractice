# The least distance is a straight line.

import sys
x, y, w, h = map(int, sys.stdin.readline().split())
# Print the least distance of each straight line
print(min([x, y, w-x, h-y]))