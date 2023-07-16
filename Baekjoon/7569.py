import sys
from collections import deque

read = sys.stdin.readline
m, n, h = map(int, read().rstrip().split())

queue = deque()
graph = []
for nh in range(h):
    box = []
    for nn in range(n):
        tomatoes = list(map(int, read().rstrip().split()))
        box.append(tomatoes)
        for i in range(m):
            if tomatoes[i] == 1:
                queue.append([i, nn, nh])
    graph.append(box)

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(queue):
    day = 0
    while(queue):
        cx, cy, cz = queue.popleft()
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            if graph[nz][ny][nx] == -1:
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[cz][cy][cx] + 1
                queue.append([nx, ny, nz])
                day = max(day, graph[nz][ny][nx])

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    print(-1)
                    return

    if day == 0:
        print(0)
    else:
        print(day-1)
    return
bfs(queue)
