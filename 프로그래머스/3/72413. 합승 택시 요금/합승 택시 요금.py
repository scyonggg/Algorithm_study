from heapq import heappush, heappop
import math

INF = math.inf

def debug_2d(graph):
    for i, g in enumerate(graph, start=1):
        print(i, g)
    print()

def dijkstra(src, graph):
    '''
    src부터 dest까지 가는 최소 요금
    '''
    hq = []
    visit = [INF] * len(graph)
    heappush(hq, (0, src))
    visit[src] = 0
    while hq:
        c_cost, cur = heappop(hq)
        for idx, fare in enumerate(graph[cur]):
            if fare == -1:
                continue
            n_cost = c_cost + fare
            if n_cost < visit[idx]:
                visit[idx] = n_cost
                heappush(hq, (n_cost, idx))
    return visit


def solution(n, s, a, b, fares):
    
    answer = 0
    graph = [[-1] * (n+1) for _ in range(n+1)]  # graph[i][j] : i부터 j까지 요금. -1이면 갈 수 없음.
    for fare in fares:
        x, y, cost = fare
        graph[x][y] = cost
        graph[y][x] = cost

    # s에서 출발했을 때 나머지 노드들까지 걸리는 요금
    fares_s2n = dijkstra(s, graph)
    
    # 각 노드에서 A, B로 이동할 때 걸리는 요금.
    fares_n2a = dijkstra(a, graph)
    fares_n2b = dijkstra(b, graph)
    
    # s에서 출발해서 i를 거쳐 A, B로 이동할 때 요금
    fares_together = [fares_s2n[i] + fares_n2a[i] + fares_n2b[i] for i in range(1, n+1)]
    min_fares_together = min(fares_together)
    
    # 각자 택시 탑승
    individual_fare = fares_s2n[a] + fares_s2n[b]
    
    if individual_fare < min_fares_together:
        return individual_fare
    else:
        return min_fares_together
    
    
