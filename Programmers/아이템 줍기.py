from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    graph = [[5] * (MAX) for _ in range(MAX)]

    for point in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, point)

        for row in range(y1, y2 + 1):
            for col in range(x1, x2 + 1):
                if y1 < row < y2 and x1 < col < x2:  # 내부
                    graph[row][col] = 0
                elif graph[row][col] != 0:  # 내부가 아니면서 다른 직사각형의 내부도 아닐 때 : 테두리
                    graph[row][col] = 1

    visit = [[0] * MAX for _ in range(MAX)]

    q = deque()
    q.append((characterX * 2, characterY * 2))
    visit[characterY * 2][characterX * 2] = 1

    while q:
        cx, cy = q.popleft()
        if cx == itemX * 2 and cy == itemY * 2:
            answer = visit[cy][cx] // 2
            break
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx = cx + dx
            ny = cy + dy
            if ny < 0 or ny >= MAX or nx < 0 or nx >= MAX:
                continue
            if graph[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = visit[cy][cx] + 1
                q.append((nx, ny))

    return answer