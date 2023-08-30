import sys
from heapq import heappush, heappop

read = sys.stdin.readline

V, E = map(int, read().rstrip().split())
k = int(read().rstrip())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, read().rstrip().split())
    graph[u].append((w, v))  # (cost, dest)

INF = int(1e9)
distance = [INF] * (V+1)
pq = []
heappush(pq, (0, k))
distance[k] = 0

while pq:
    dist, node = heappop(pq)
    if distance[node] < dist:
        continue
    for nxt_cost, nxt_dest in graph[node]:
        cost = distance[node] + nxt_cost
        if cost < distance[nxt_dest]:
            distance[nxt_dest] = cost
            heappush(pq, (cost, nxt_dest))

for i in range(1, V+1):
    ans = distance[i]
    if ans == INF:
        print('INF')
    else:
        print(ans)