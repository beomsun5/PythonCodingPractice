# What should be considered once more is g and h may not be adjacent, so the shortest path between
# 'g' and 'h' has to be found
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
def Dijsktra(start):
  dest = [INF]*(n+1)
  dest[start] = 0
  heap = []
  heapq.heappush(heap, (0, start))
  while heap:
    wei, now = heapq.heappop(heap)
    if dest[now] < wei:
      continue
    for w, next_node in graph[now]:
      next_wei = wei + w
      if next_wei < dest[next_node]:
        dest[next_node] = next_wei
        heapq.heappush(heap, (next_wei, next_node))
  return dest
    
# T : Number of test cases
T = int(input())
for _ in range(T):
  # n : number of intersections (vertex) / m : number of roads (edges)
  # t : number of places the thieves are supposed to go
  n, m, t = map(int, input().split())
  graph = [[] for i in range(n+1)]
  # goOrNot : the places related to 't'
  goOrNot = []
  # s : starting vertex / g, h : vertices which should be selected within the shortest path
  s, g, h = map(int, input().split())
  for _ in range(m):
    # a, b : vertices / d : distance between a and b
    a, b, d = map(int, input().split())
    # This graph consists of both directed edges, so there are not start and end.
    graph[a].append((d, b))
    graph[b].append((d, a))
  for _ in range(t):
    goOrNot.append(int(input()))
  goOrNot.sort()
  # fromS, fromG, fromH : Shortest Path from s, g, h
  fromS = Dijsktra(s)
  fromG = Dijsktra(g)
  fromH = Dijsktra(h)
  for idx in goOrNot:
    # If the sum of each shortest path equals to the shortest path from the start and the end,
    # it is plausible for the thieves to arrive at the destination through 'g' and 'h'.
    # If this condition is satisfied, 'idx' is printed.
    if fromS[g] + fromG[h] + fromH[idx] == fromS[idx] or fromS[h] + fromH[g] + fromG[idx] == fromS[idx]:
      print(idx, end = " ")
  print()

''' <My solution> -> What I considered as conditions are the shortest path should pass by 'g' and 'h'
                     So, I just got the shortest path from the starting vertex to the destination
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
# T : Number of test cases
T = int(input())
for _ in range(T):
  # n : number of intersections (vertex) / m : number of roads (edges)
  # t : number of places the thieves are supposed to go
  n, m, t = map(int, input().split())
  dest = [INF]*(n+1)
  graph = [[] for i in range(n+1)]
  # visited : the list storing the intersections on the shortest path
  visited = [[] for i in range(n+1)]
  # goOrNot : the places related to 't'
  goOrNot = []
  # s : starting vertex / g, h : vertices which should be selected within the shortest path
  s, g, h = map(int, input().split())
  for _ in range(m):
    # a, b : vertices / d : distance between a and b
    a, b, d = map(int, input().split())
    # This graph consists of both directed edges, so there are not start and end.
    graph[a].append((d, b))
    graph[b].append((d, a))
  def Dijsktra(start):
    dest[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
      wei, now = heapq.heappop(heap)
      if dest[now] < wei:
        continue
      for w, next_node in graph[now]:
        next_wei = wei + w
        if next_wei < dest[next_node]:
          dest[next_node] = next_wei
          if now == start:
            visited[next_node].append(now)
          else:
            visited[next_node] = visited[now].copy()
            visited[next_node].append(now)
          heapq.heappush(heap, (next_wei, next_node))
  Dijsktra(s)
  for _ in range(t):
    goOrNot.append(int(input()))
  goOrNot.sort()
  for idx in goOrNot:
    if g and h in visited[idx]:
      print(idx, end = " ")
  print()
'''