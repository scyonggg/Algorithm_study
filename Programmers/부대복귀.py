### Dijkstra 풀이
import heapq

def solution(n, roads, sources, destination):
    answer = []

    graph = [[] for _ in range(n+1)]
    for road in roads:
        graph[road[0]].append((1, road[1]))
        graph[road[1]].append((1, road[0]))
    
    INF = int(1e9)
    distance = [INF] * (n+1)
    
    pq = []
    heapq.heappush(pq, (0, destination))
    distance[destination] = 0
    
    while pq:
        dist, cur = heapq.heappop(pq)
        if dist > distance[cur]:
            continue
        for nxt_dist, nxt_node in graph[cur]:
            cost = nxt_dist + distance[cur]
            if cost < distance[nxt_node]:
                distance[nxt_node] = cost
                heapq.heappush(pq, (cost, nxt_node))
                
    for source in sources:
        if distance[source] == INF:
            answer.append(-1)
        else:
            answer.append(distance[source])
            
    return answer

""" BFS 풀이
from collections import deque

def solution(n, roads, sources, destination):
    answer = []

    graph = [[] for _ in range(n + 1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    visit = [-1] * (n + 1)
    visit[destination] = 0
    q = deque()
    q.append(destination)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visit[nxt] == -1:
                visit[nxt] = visit[cur] + 1
                q.append(nxt)

    for source in sources:
        answer.append(visit[source])
    return answer
"""