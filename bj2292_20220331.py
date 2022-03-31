import sys
n = int(sys.stdin.readline())     # Room Number
roomCount = 1                     # Show the total roooms that we have passed
stdroomNum = 1                    # Checking point of the room Number
while 1:
  # If room number is 1, the number of room that we have passed is 1
  if n == 1:               
    print(1)
    break
  # If room number is more than 1
  else:
    if stdroomNum < n <= stdroomNum + 6 * roomCount:
      print(roomCount+1)
      break
    else:
      stdroomNum += 6 * roomCount
      roomCount += 1
'''
The patter is like this,
 2 ~  7 :  6 numbers (6 * <1>) -> 2 rooms should be passed (1 + <1>)
 8 ~ 19 : 12 numbers (6 * <2>) -> 3 rooms should be passed (1 + <2>)
20 ~ 37 : 18 numbers (6 * <3>) -> 4 rooms should be passed (1 + <3>)
...
'''