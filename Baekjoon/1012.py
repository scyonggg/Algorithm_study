from collections import deque
import sys

read = sys.stdin.readline

T = int(read().rstrip())

for _ in range(T):
    M, N, K = map(int, read().rstrip().split())
    graph = [[0] * M for _ in range(N)]
    for k in range(K):
        X, Y = map(int, read().rstrip().split())
        graph[Y][X] = 1

    visit = [[0] * M for _ in range(N)]
    def bfs(x, y, cnt):
        q = deque()
        q.append((x, y))
        visit[y][x] = cnt

        while q:
            cx, cy = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx = cx + dx
                ny = cy + dy
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if visit[ny][nx] == 0 and graph[ny][nx] == 1:
                    visit[ny][nx] = cnt
                    q.append((nx, ny))

    groups = 0
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 1 and visit[n][m] == 0:
                groups += 1
                bfs(m, n, groups)

    print(groups)
