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