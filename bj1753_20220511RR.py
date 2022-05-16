# Success - Dijsktra's algorithm using priority heap
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
# 시작점 K
K = int(input())
# 가중치 테이블 dp
dp = [INF] * (V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
  # 가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
  dp[start] = 0
  heapq.heappush(heap, (0, start)) # (가중치, 도착지점) tuple 형태의 자료 형태로 heappush
  # 힙에 원소가 없을 때까지 반복
  while heap:
    wei, now = heapq.heappop(heap)
    # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시
    # 최단 거리를 계산하는데, 우선순위 큐에서 pop한 가중치(거리)가 현재 최소 거리보다 크다면, 비교가 의미 없으므로 다음 요소로 넘어가는 것!
    # (현재 노드가 이미 처리된 적이 있다면 무시.....(?!))
    # heap에는 '특정 목적지에 대한 더 짧은 거리가 계산된 경우의 거리' 혹은 '인접한 노드에 대한 거리'가 들어간다.
    # 따라서 불필요한 부분에 대한 메모리 소모가 없고, 거리 계산 과정 중에 나오는 노드와 거리에 대한 요소들에 대해서만 비교를 하기 때문에
    # 불필요한 메모리 소모를 줄일 수 있다.
    if dp[now] < wei:
      continue
    for w, next_node in graph[now]:
      # 현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next node)까지의 가중치 w
      # = 다음 노드까지의 가중치(next_wei)
      next_wei = w + wei
      # 다음 노드까지의 가중치(next-wei)가 현재 기록된 값보다 작으면 조건 성립.
      if next_wei < dp[next_node]:
        # 계산했던 next_wei를 가중치 테이블에 업데이트.
        dp[next_node] = next_wei
        # 다음 점까지의 가중치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
        heapq.heappush(heap, (next_wei, next_node))
# 초기화
for _ in range(E):
  u, v, w = map(int, input().split())
  # (가중치, 목적지 노드) 형태로 저장
  graph[u].append((w, v))

Dijkstra(K)
for i in range(1, V+1):
  print("INF" if dp[i] == INF else dp[i])

''' 1st Code written right after understanding dijsktra's algorithm with priority Queue
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((w, v))
def Dijsktra(start):
  heap = []
  distance[start] = 0
  heapq.heappush(heap, (0, start))
  while heap:
    wei, now = heapq.heappop(heap)
    if distance[now] < wei:
      continue
    for w, next_v in graph[now]:
      next_wei = wei + w
      if next_wei < distance[next_v]:
        distance[next_v] = next_wei
        heapq.heappush(heap, (next_wei, next_v))
Dijsktra(K)
for i in range(1, V+1):
  print("INF" if distance[i] == INF else distance[i])
'''

''' Fail (Memory Excession) - Using Graph Adjacency Matrix (Conventional Dijsktra algorithm)
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = 10**6
g = [[0]*V for i in range(V)]

for _ in range(E):
  u, v, w = map(int, input().split())
  g[u-1][v-1] = w

def minDistance(distance, sptSet):
  min = INF
  min_index = None
  for vt in range(V):
    # distance[vt] does not need to be equal to or less than 'min' (Just less than is enough for this condition)
    if (sptSet[vt] == 0 and distance[vt] <= min):
      min = distance[vt]
      min_index = vt
  return min_index

def dijkstra():
  distance = [INF]*V
  sptSet = [0]*V
  distance[K-1] = 0
  for i in range(V-1):
    u = minDistance(distance, sptSet)
    sptSet[u] = 1
    # u : current vertex (shortest distance will be selected soon)
    # v : traversing each end of the edges whose starting vertex is 'u'
    for v in range(V):
      # Condition
      # 1. if vertex 'v' is not in the 'sptSet'
      # 2. if there is any distance (more than 0) in the adjacency matrix graph 'u-v'
      # 3. if the current vertex distance value is not INF
      # 4. if vertex 'v' distance value is larger than the sum of vertex 'u' distance value and the 'u-v' edge value.
      # If those 4 conditions above are all satisfied, update the distance value of vertex 'v'
      if (not sptSet[v] and g[u][v] and distance[u] != INF and distance[u] + g[u][v] < distance[v]):
        distance[v] = distance[u] + g[u][v]
  for i in range(len(distance)):
    if distance[i] == INF:
      print('INF')
    else:
      print(distance[i])
dijkstra()
'''