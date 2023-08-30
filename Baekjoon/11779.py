import sys
from heapq import heappush, heappop
from collections import deque

read = sys.stdin.readline

n = int(read().rstrip())
m = int(read().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, read().rstrip().split())
    graph[s].append((c, e))

start, end = map(int, read().rstrip().split())

INF = int(1e9)
distance = [INF] * (n+1)
prev = [0] * (n+1)
answer = []

pq = []
heappush(pq, (0, start))
distance[start] = 0

while pq:
    dist, node = heappop(pq)
    if distance[node] < dist:
        continue
    for next_cost, next_node in graph[node]:
        cost = distance[node] + next_cost
        if cost < distance[next_node]:
            prev[next_node] = node
            distance[next_node] = cost
            heappush(pq, (cost, next_node))

print(distance[end])
# print(prev)

answer.append(end)
cursor = end
while cursor != start:
    cursor = prev[cursor]
    answer.append(cursor)

print(len(answer))
for idx in range(len(answer)-1, -1, -1):
    print(answer[idx], end=' ')
