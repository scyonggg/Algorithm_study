from collections import deque
def solution(maps):
    answer = 0
    
    height = len(maps)
    width = len(maps[0])
    
    graph = [[None] * width for _ in range(height)]
    visit = [[[-1] * width for _ in range(height)] for _ in range(2)]
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'S':
                start = (x, y)
            graph[y][x] = maps[y][x]
                
    q = deque()
    q.append((start[0], start[1]))
    visit[0][start[1]][start[0]] = 0
    flag = False
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx = cx + dx
            ny = cy + dy
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            if flag:
                if visit[1][ny][nx] == -1 and not graph[ny][nx] == 'X':
                    
                    if graph[ny][nx] == 'E':
                        return visit[1][cy][cx] + 1
                    visit[1][ny][nx] = visit[1][cy][cx] + 1
                    q.append((nx, ny))
            else:  # 레버 당겼을 때 
                if visit[0][ny][nx] == -1 and not graph[ny][nx] == 'X':
                    if graph[ny][nx] == 'L':
                        flag = True
                        visit[1][ny][nx] = visit[0][cy][cx] + 1
                        q.clear()
                        q.append((nx, ny))
                        break  # 레버 당긴 순간 다른 방향 탐색은 중단.
                    else:
                        visit[0][ny][nx] = visit[0][cy][cx] + 1
                        q.append((nx, ny))
    
    return -1
