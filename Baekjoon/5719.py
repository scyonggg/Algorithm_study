import sys
from heapq import heappush, heappop
from collections import deque

read = sys.stdin.readline
INF = sys.maxsize

while True:
    n, m = map(int, read().rstrip().split())
    if n == 0 and m == 0:
        break
    s, d = map(int, read().rstrip().split())

    graph = [[] for _ in range(n)]
    graph_back = [[] for _ in range(n)]
    available = [[True] * n for _ in range(n)]
    distance = [INF] * n

    for _ in range(m):
        u, v, p = map(int, read().rstrip().split())
        graph[u].append([p, v])  # dist, node
        graph_back[v].append([p, u])

    def dijkstra(start, end):
        pq = []
        heappush(pq, (0, start))
        distance[start] = 0

        while pq:
            dist, node = heappop(pq)
            if distance[node] < dist:
                continue
            if node == end:
                break
            for next_dist, next_node in graph[node]:
                cost = next_dist + dist
                if cost < distance[next_node] and available[node][next_node]:
                    distance[next_node] = cost
                    heappush(pq, (cost, next_node))
    
        return distance[end]

    # 도착지부터 출발지까지 역으로 BFS
    def bfs(start, dest):
        q = deque()
        visit = [-1] * n
        q.append((0, dest))
        visit[dest] = 0

        while q:
            cost, cx = q.popleft()
            for dist, node in graph_back[cx]:
                # 출발지 ~ node : distance[node]
                # node ~ cx : cost
                # cx ~ 도착지 : dist
                # 즉, 위 세개를 더하면 출발지 ~ 도착지가 되고, 그것이 최소 경로 (distance[dest]) 일 경우, 도로를 제거한다.
                if dist + distance[node] + cost == distance[dest]:
                    available[node][cx] = False
                    available[cx][node] = False
                    if visit[node] == -1:
                        visit[node] = 0
                        q.append((cost+dist, node))


    dist = dijkstra(s, d)
    if dist == INF:
        print(-1)
        continue
    bfs(s, d)
    distance = [INF] * n
    dist2 = dijkstra(s, d)
    if dist2 == INF:
        print(-1)
    else:
        print(dist2)
