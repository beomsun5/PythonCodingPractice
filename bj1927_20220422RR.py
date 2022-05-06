'''
# <My solution> - 2nd trial -> Compiling time Exceeded (Creating minimum heap function)
# Referred to Trello pseudocode
import sys

# How to make the function of heap sort (Min Heap Ver.)
def min_heap(arr):
  def min_heapify(idx, l):  # l : Maximum index of the heap + 1 == The size of heap
    least_idx = idx
    left, right = idx * 2 + 1, idx * 2 + 2
    if left < l and arr[least_idx] > arr[left]:
      least_idx = left
    if right < l and arr[least_idx] > arr[right]:
      least_idx = right
    if least_idx != idx:
      arr[idx], arr[least_idx] = arr[least_idx], arr[idx]
      min_heapify(least_idx, l)

  n = len(arr)
  for idx in range(n//2-1, -1, -1):
    min_heapify(idx, n)
  for i in range(n-1, 0, -1):
    min_heapify(0, i)     # 0부터 i-1까지 heapify

  return arr

n = int(sys.stdin.readline())
cmd_list = []
data_list = []
for i in range(n):
  cmd_list.append(int(sys.stdin.readline()))
for cmd in cmd_list:
  if cmd == 0:
    if len(data_list) == 0:
      print(0)
    else:
      data_list = min_heap(data_list)   # heapify : make the list heap
      print(data_list[0])               # heappop : pop the smallest value of the list, automatically heapify the list
      del data_list[0]                  # Before executing heappop(), the given list is not heap, unless you make it heap.
  else:
    data_list.append(cmd)
'''
# <My Solution> - using heapq library
import sys
import heapq
# Repitition number of the loop
n = int(sys.stdin.readline())
data_list = []
for i in range(n):
  data = int(sys.stdin.readline())
  if data:
    heapq.heappush(data_list, data)              # To reduce the compiling time, heappush is more efficient than append()
                                                 # If you use heappush, it makes data_list heap. (Don't have to heapify intentionally)
  else:
    if data_list:
      heapq.heapify(data_list)
      print(heapq.heappop(data_list))
    else:
      print(0)
# heapify : make the list heap
# heappop : pop the smallest value of the list, automatically heapify the list
# Before executing heappop(), the given list is not heap, unless you make it heap.