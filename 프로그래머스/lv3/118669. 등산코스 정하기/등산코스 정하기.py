""" Dijkstra """
import sys
from collections import deque
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    answer = []
    INF = sys.maxsize
    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    
    for path in paths:
        s, e, c = path
        graph[s].append([c, e])  # graph[출발] = 시간, 도착
        graph[e].append([c, s])

    is_summit = [False] * (n+1)
    for summit in summits:
        is_summit[summit] = True
        
    q = []  # cost, node
    for gate in gates:
        distance[gate] = 0
        heappush(q, (0, gate))
        
    while q:
        dist, node = heappop(q)
        if distance[node] < dist or is_summit[node]:  # 다음 node까지 시간이 distance 행렬보다 크면 갈 필요가 없다.
            continue
        
        for ndist, nnode in graph[node]:
            cost = max(ndist, distance[node])
            if cost < distance[nnode]:
                distance[nnode] = cost
                heappush(q, (cost, nnode))
    
    summits.sort()
    intensity = INF
    min_summit = 0
    for summit in summits:
        if distance[summit] < intensity:
            intensity = distance[summit]
            min_summit = summit
    
    answer = [min_summit, intensity]
    return answer











