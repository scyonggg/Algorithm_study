import sys
from collections import deque

# n, m = map(int, input().split())
read = sys.stdin.readline
m, n = map(int, read().rstrip().split())  # n : # of rows, m : # of cols

q = deque()
graph = []
for i in range(n):
    graph.append(list(map(int, read().rstrip().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[0] * m for _ in range(n)]

def bfs(queue):
    day = 0
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == -1:
                continue
            if graph[ny][nx] == 1:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[cy][cx] + 1
                queue.append([ny, nx])
                day = max(day, graph[ny][nx])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
    if day == 0:
        return 0
    else:
        return day-1

day = bfs(q)
print(day)

