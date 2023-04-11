from collections import deque


def bfs(x, y, m, n, maps, visit):
    """
    x, y : 현재 위치
    m, n : 최대 범위 (m: row, n: col)
    """
    if maps[y][x] == 'X':
        return 0
    Q = deque()
    Q.append((x, y))
    ans = 0
    if not visit[y][x]:
        ans += int(maps[y][x])
        visit[y][x] = True

    while Q:
        cx, cy = Q.popleft()
        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx = cx + dx
            ny = cy + dy

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if maps[ny][nx] == 'X':
                continue

            if visit[ny][nx] == False:
                visit[ny][nx] = True
                ans += int(maps[ny][nx])
                Q.append((nx, ny))

    return ans


def solution(maps):
    n = len(maps)  # col 방향 최대 범위
    m = len(maps[0])  # row 방향 최대 범위

    visit = [[False] * m for _ in range(n)]

    answer = []

    for i in range(n):  # col
        for j in range(m):  # row
            ans = bfs(j, i, m, n, maps, visit)
            if ans != 0:
                answer.append(ans)

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer