import sys
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))
    # distance = 1
    visit[0][0][0] = 1
    visit[1][0][0] = 1
    while queue:
        cx, cy, broken = queue.popleft()
        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx = cx + dx
            ny = cy + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if broken == 0 and visit[0][ny][nx] != 0:
                continue
            if broken == 1 and visit[1][ny][nx] != 0:
                continue
            if graph[ny][nx] == 0:  # 접근 가능한 길
                if broken == 0:
                    visit[0][ny][nx] = visit[0][cy][cx] + 1
                elif broken == 1:
                    visit[1][ny][nx] = visit[1][cy][cx] + 1
                queue.append((nx, ny, broken))
            elif graph[ny][nx] == 1:  # 접근 불가능한 벽
                if broken == 0:  # 벽을 깬 적이 없어야만 갈 수 있다.
                    visit[1][ny][nx] = visit[0][cy][cx] + 1
                    queue.append((nx, ny, 1))
                else:
                    continue
    return visit[0][n-1][m-1], visit[1][n-1][m-1]

read = sys.stdin.readline
n, m = map(int, read().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, read().rstrip())))

# visit[0] : 벽을 깨지 않은 visit 배열
# visit[1] : 벽을 깬 visit 배열
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

result1, result2 = bfs(0, 0)
if result1 == 0:
    if result2 == 0:
        print(-1)
    else:
        print(result2)
elif result2 == 0:
    print(result1)
else:
    print(min(result1, result2))
