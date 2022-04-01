import sys, math
a, b, v = map(int, sys.stdin.readline().split())
if a > b:
  dayCount = math.ceil(1 + (v - a) / (a - b))     # math.ceil() : 올림 함수
  print(dayCount)

'''
a : height going up during the day
b : height going down during the night
a - b : height the snail moved during 1 day (the past)
d : The days that the snail approach the summit of the bar after starting from the bottom.

Therefore, this formula is established,

(a - b) * (d - 1) + a >= v

d >= 1 + (v - a) / (a - b) (If, a > b)
'''