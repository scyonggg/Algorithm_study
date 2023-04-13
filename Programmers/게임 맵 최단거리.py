from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    def bfs(x, y):
        Q = deque()
        Q.append((x, y))
        visited[y][x] = 1
        while Q:
            cx, cy = Q.popleft()
            
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx = cx + dx
                ny = cy + dy
                
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if maps[ny][nx] != 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    Q.append((nx, ny))
    
    
    
    bfs(0, 0)
    answer = visited[n-1][m-1]
    if answer == 0:
        answer = -1
    return answer