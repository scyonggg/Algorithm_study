import sys
from collections import deque

read = sys.stdin.readline

n, m = list(map(int, read().rstrip().split()))
miro = []
for i in range(n):
    line = list(map(int, read().rstrip()))
    miro.append(line)

visit = [[0] * m for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[y][x] = 1
    while q:
        cx, cy = q.popleft()
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx = cx + dx
            ny = cy + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if miro[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = visit[cy][cx] + 1
                q.append((nx, ny))

bfs(0, 0)
print(visit[n-1][m-1])