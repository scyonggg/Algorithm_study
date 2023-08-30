import sys
import heapq

read = sys.stdin.readline

n = int(read().rstrip())
m = int(read().rstrip())

graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end, cost = map(int, read().rstrip().split())
    graph[start].append((cost, end))

start, end = map(int, read().rstrip().split())
INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, cur_node = heapq.heappop(pq)
        if distance[cur_node] < cost:
            continue
        for next_node in graph[cur_node]:
            dist = distance[cur_node] + next_node[0]
            if dist < distance[next_node[1]]:
                distance[next_node[1]] = dist
                heapq.heappush(pq, (dist, next_node[1]))

dijkstra(start)
print(distance[end])
        