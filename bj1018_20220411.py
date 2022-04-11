# Did not solve it on my own. Review it.
import sys

N, M = map(int, sys.stdin.readline().split())
original_board = []
count_Coloring = []

for i in range(N):
  original_board.append(sys.stdin.readline().rstrip())

# rStart, cStart : starting point of checking the board
for rStart in range(N-7):
  for cStart in range(M-7):
    # check1 : starting point character is 'W', check2 : starting point character is 'B'
    check1 = 0
    check2 = 0
    # row, column : check 8X8 size of the board starting from (rStart, cStart).
    for row in range(rStart, rStart+8):
      for column in range(cStart, cStart+8):
        # check (row, column) location of which sum is even
        if ((row+column) % 2 == 0):
          if original_board[row][column] != 'B':
            check1 += 1
          if original_board[row][column] != 'W':
            check2 += 1
        # check (row, column) location of which sum is odd
        else:
          if original_board[row][column] != 'W':
            check1 += 1
          if original_board[row][column] != 'B':
            check2 += 1
    # Choose the less one
    count_Coloring.append(min(check1, check2))
    '''
    #Check1 : Compare the given board to this board and count the number of different parts
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    #Check2 : Compare the given board to this board and count the number of different parts
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    '''
# Compare the number of all possible cases and print the minimum.
print(min(count_Coloring))

'''
# Did not pass 2022.04.01
import sys

def checkReColorSpot(r_list, rowNum, colNum):
  stdBoard = []
  # Size : 8 * 8
  if rowNum == 8 & colNum == 8:
    reColorSpot1 = 0
    reColorSpot2 = 0
    # The first element : 'W'    
    stdBoard1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    # The first element : 'B'
    stdBoard2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
    # Comparing with stdBoard1 and stdBoard2
    for r in range(rowNum):
      for c in range(colNum):
        if r_list[r][c] != stdBoard1[r][c]: reColorSpot1 += 1
        if r_list[r][c] != stdBoard2[r][c]: reColorSpot2 += 1
    return min(reColorSpot1, reColorSpot2)
  # Size : >8 * >8 (either or all of them are more than 8)
  else:
    minReColorSpot = 32 # The maximum of refilling the color is 32.
    for rStart in range(rowNum-7):
      for cStart in range(colNum-7):
        # The first element : 'W'
        stdBoard1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
        # The first element : 'B'
        stdBoard2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
        # Comparing with stdBoard1
        reColorSpot = 0
        for r in range(rStart, rStart+8):
          for c in range(cStart, cStart+8):
            if r_list[r][c] != stdBoard1[r-rStart][c-cStart]: reColorSpot += 1
        if minReColorSpot > reColorSpot: minReColorSpot = reColorSpot
        # Comparing with stdBoard2
        reColorSpot = 0
        for r in range(rStart, rStart+8):
          for c in range(cStart, cStart+8):
            if r_list[r][c] != stdBoard2[r-rStart][c-cStart]: reColorSpot += 1
        if minReColorSpot > reColorSpot: minReColorSpot = reColorSpot
    return minReColorSpot


m, n = map(int, sys.stdin.readline().split())
row_list = []
for i in range(m):
  row_list.append(sys.stdin.readline().strip())
print(checkReColorSpot(row_list, m, n))


# Documentation
Perfect form of the chess board is like one of these:

WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB
WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB
WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB
WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB

Set one of these as a standard form and compare the given material to the standard.

If the board size is more than 8*8, change the starting point and get the number of the spots.

'''