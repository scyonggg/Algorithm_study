import sys
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().rstrip().split())

graph = [list(map(int, read().rstrip().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
day = 0

def bfs(x, y, melt):
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] > 0 and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append((nx, ny))
            elif graph[ny][nx] == 0:
                melt[y][x] += 1
    return 1

year = 0
flag = False
while True:
    visited = [[False] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visited[i][j] == False:
                result.append(bfs(j, i, melt))

    # Melt ice mountain
    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - melt[i][j])

    if len(result) == 0:
        break
    if len(result) >= 2:
        flag = True
        break
    year += 1

if flag:
    print(year)
else:
    print(0)