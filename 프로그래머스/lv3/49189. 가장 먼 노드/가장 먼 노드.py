from collections import deque, Counter
def solution(n, edge):
    answer = 0
    
    graph = [[] * (n+1) for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visit = [0] * (n+1)
        
    q = deque()
    q.append(1)
    visit[1] = 1
    while q:
        cx = q.popleft()
        
        for node in graph[cx]:
            if visit[node] != 0:
                continue
            visit[node] = visit[cx] + 1
            q.append(node)
    
    maxi = max(visit)
    answer = Counter(visit)[maxi]
    
    return answer