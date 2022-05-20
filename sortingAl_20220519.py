'''
Sorting Algorithm Practice Code : All codes are based on the ascending order
'''
'''
# Insertion Sort
arr = [2, 9, 3, 1, 0, 5, 6]
def Insertion_Sort():
  # Increment the last index of the sorted subarray until the end of the loop
  # However, in fact, 'end' is the element that we want to put in the right position
  # -> The array within the range of [0, end-1] is the sorted subarray
  for end in range(1, len(arr)):
    # From the last element of the sorted subarray, check the 2 elements next to each other
    # and swap them if they are not in the right order.
    for i in range(end, 0, -1):
      if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
      print("end = %d, i = %d"%(end, i))
      print(arr)
      print()
Insertion_Sort()
print("Result : ", end = "")
print(arr)
'''
'''
# Quick Sort : "Pivot"
arr = [2, 9, 3, 1, 0, 5, 6]
def Quick_Sort():
  def sort(low, high):
    if high <= low:
      return
    mid = partition(low, high)
    sort(low, mid - 1)
    sort(mid, high)
  def partition(low, high):
    pivot = arr[(low + high) // 2] # Median of the first and the last index
    while low <= high:
      while arr[low] < pivot: low += 1
      while arr[high] > pivot: high -= 1
      if low <= high:
        arr[low], arr[high] = arr[high], arr[low]
        low, high = low + 1, high - 1
    return low
  return sort(0, len(arr) - 1) # len(arr) - 1 == the last index of the array
Quick_Sort()
print(arr)
'''
'''
# Merge Sort : Partition and Merge
arr = [2, 9, 3, 1, 0, 5, 6]
def Merge_Sort(arr):
  if len(arr) < 2:
    return arr
  mid = len(arr) // 2
  low_arr = Merge_Sort(arr[:mid])
  high_arr = Merge_Sort(arr[mid:])

  merged_arr = []
  l = h = 0
  while l < len(low_arr) and h < len(high_arr):
    print("current array : ", end="")
    print(arr, end="\n\n")
    if low_arr[l] < high_arr[h]:
      merged_arr.append(low_arr[l])
      l += 1
    else:
      merged_arr.append(high_arr[h])
      h += 1
  merged_arr += low_arr[l:]
  merged_arr += high_arr[h:]
  print("<After Merged>")
  print("l : %d, h : %d"%(l, h))
  print("low array : ", end="")
  print(low_arr)
  print("high array : ", end="")
  print(high_arr)
  print("merged array : ", end="")
  print(merged_arr, end="\n\n")
  return merged_arr
arr = Merge_Sort(arr)
print(arr)
'''
'''
# Heap Sort : Using Max-Heap
# Repeat making the array into the max heap and getting the root of the heap!
# Whenever change the element of the first and the last element of the max heap
# and heapify the subarray except the last element,
# you will get the sorted array (in an ascending order)
arr = [2, 9, 3, 1, 0, 5, 6]
def Heap_Sort(arr):
  def heapify(i, l):  # i : the index of the present node / l : the value of the present node
    largest = i
    left, right = i * 2 + 1, i * 2 + 2
    if left < l and arr[largest] < arr[left]:
      largest = left
    if right < l and arr[largest] < arr[right]:
      largest = right
    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(largest, l)

  n = len(arr)
  for idx in range(n // 2 - 1, -1, -1):
    heapify(idx, n)
  arr[0], arr[n-1] = arr[n-1], arr[0]     # Added code
  for i in range(n - 1, 0, -1):
    heapify(0, i) # 0 ~ i-1 heapify
    arr[0], arr[i-1] = arr[i-1], arr[0]   # Added code
  return arr

arr = Heap_Sort(arr)
print(arr)
'''
'''
# Counting Sort (계수 정렬)
# Necessary Condition -> K : the size of 'c' is determined by the largest value of the array --> Could waste the memory
# If K is less than the largest value of the array, it is restricted to access 'c' because there may be a value out of list index.
def Counting_Sort(arr, K):
  c = [0] * K
  sorted_arr = [0] * len(arr)
  for i in arr:
    c[i] += 1
  for i in range(1, K):
    c[i] += c[i-1]
  for i in range(len(arr)):
    sorted_arr[c[arr[i]]-1] = arr[i]
    c[arr[i]] -= 1
  return sorted_arr

arr = [3, 5, 1, 2, 9, 6, 4, 7, 5]
print(Counting_Sort(arr, 20))
# Result : [1, 2, 3, 4, 5, 5, 6, 7, 9]
'''
'''
# Radix Sort (기수 정렬)
# This sorting algorithm uses counting sort algorithm as a part of itself.
# In the courting sort algorithm, there should be 'queues' for each digit.
# While this algorithm is being executed, the numbers with the same digit become sorted.
from collections import deque

def Radix_Sort(arr):
  maxValue = max(arr)
  digit = 1
  while int(maxValue/digit) > 0:
    digit_arr = []
    for num in arr:
      digit_arr.append((num//digit)%10)
    print("Before Sorting -> Digit = %d"%(digit))
    print("arr = ", end="")
    print(arr)
    print("digit_arr = ", end="")
    print(digit_arr)
    arr = Counting_Sort(arr, digit_arr, 10)
    print("After Sorting -> Digit = %d"%(digit))
    print("arr = ", end="")
    print(arr)
    print()
    digit *= 10
  return arr

# This code is a little different from the original counting sort algorithm code,
# beware of the difference.
def Counting_Sort(arr, digit_arr, K):
  queue_list = [deque() for _ in range(K)]
  sorted_arr = []
  for i in range(len(arr)):
    queue_list[digit_arr[i]].append(arr[i])
  for i in range(len(arr)):
    while len(queue_list[i]) > 0:
      sorted_arr.append(queue_list[i].popleft())
  return sorted_arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
arr = Radix_Sort(arr)
print(arr)
'''
'''
# 'List' Method for Sorting
# 1. reverse : just reverse the order of the list (Not meaning descending order)
a = [1, 10, 5, 7, 6]
a.reverse()
print(a)
# 2. sort : arranging the list elements in a specific order (Default : ascending order)
#           if 'reverse = True', descending order)
a = [1, 10, 5, 7, 6]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# 3. sort - 'key' option : According to the 'key' option, the list is sorted
m = '나는 파이썬을 잘하고 싶다'
m = m.split()
m.sort(key=len)
print(m)
# 4. sorted() : Get the reversed order of the array (Not changing the original array)
x = [1, 11, 2, 3]
y = sorted(x)
print(x)
print(y)
# 5. reversed() : This method is similar to the sorted(), but it returns iterable object.
#                 Therefore, casting the list type to the object is inevitable to find out if it is executed well.
x = [1, 11, 2, 3] # x : list
y = reversed(x)   # y : iterable object
print(list(y))
'''