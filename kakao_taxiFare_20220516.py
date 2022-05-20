''' My Solution
# Step 1 : Find the shortest path from the starting point
# Step 2 : Traverse every vertex and set each of them as the new starting point and find its shortest path
# Step 3 : Get the sum of each fare (A and B together, A alone, B alone) and compare it to the minimum fare.
#          If the sum is less than the previous result, this result becomes the minimum fare.
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n, s = 6, 4
total_fare = INF
graph = [[] for i in range(n+1)]
A, B = 6, 2
for _ in range(9):
  a, b, d = map(int, input().split())
  graph[a].append((d, b))
  graph[b].append((d, a))
def Dijkstra(start):
  dp = [INF]*(n+1)
  dp[start] = 0
  heap = []
  heapq.heappush(heap, (0, start))
  while heap:
    wei, now = heapq.heappop(heap)
    if dp[now] < wei:
      continue
    for w, next_v in graph[now]:
      next_wei = wei + w
      if next_wei < dp[next_v]:
        dp[next_v] = next_wei
        heapq.heappush(heap, (next_wei, next_v))
  return dp
for idx in range(1, n+1):
  together_fare = Dijkstra(s)
  alone_fare = Dijkstra(idx)
  total_fare = min(total_fare, together_fare[idx] + alone_fare[A] + alone_fare[B])
print(total_fare)
'''

''' Code for submitting (My solution)
import sys
import heapq
input = sys.stdin.readline

def solution(n, s, a, b, fares):
    INF = sys.maxsize
    answer = 0
    total_fare = INF
    graph = [[] for i in range(n+1)]
    for c, d, f in fares:
        graph[c].append((f, d))
        graph[d].append((f, c))
    def Dijkstra(start):
        dp = [INF]*(n+1)
        dp[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            wei, now = heapq.heappop(heap)
            if dp[now] < wei:
                continue
            for w, next_v in graph[now]:
                next_wei = wei + w
                if next_wei < dp[next_v]:
                    dp[next_v] = next_wei
                    heapq.heappush(heap, (next_wei, next_v))
        return dp
    for idx in range(1, n+1):
        together_fare = Dijkstra(s)
        alone_fare = Dijkstra(idx)
        total_fare = min(total_fare, together_fare[idx] + alone_fare[a] + alone_fare[b])
    answer = total_fare
    return answer

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
'''
# Other solution (Using Warshall-Floyd) - Need not making new function, less code
import sys
import heapq

def solution(n, s, a, b, fares):
    INF = float('inf')
    g = [[INF for _ in range(n)] for _ in range(n)]
    for x in range(n):
      g[x][x] = 0
    for c, d, f in fares:
      g[c-1][d-1] = g[d-1][c-1] = f
    for i in range(n):
      for j in range(n):
        for k in range(n):
          if g[j][k] > g[j][i] + g[i][k]:
            g[j][k] = g[j][i] + g[i][k]
    min_fare = INF
    for idx in range(n):
      if min_fare > g[s-1][idx] + g[idx][a-1] + g[idx][b-1]:
        min_fare = g[s-1][idx] + g[idx][a-1] + g[idx][b-1]
    return min_fare

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))