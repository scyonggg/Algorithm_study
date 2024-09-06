from collections import deque
def solution(land):
    """
    land[n][m]. n : 세로, m : 가로
    
    1 <= n <= 500
    1 <= m <= 500
    
    """
    answer = 0
    
    n = len(land)
    m = len(land[0])
    
    visit = [[False] * m for _ in range(n)]
    graph = [[0] * m for _ in range(n)]
    result = [0] * m
    
    def tot_oil(x, y):
        min_x = x
        max_x = x
        q = deque()
        size = 1
        q.append((x, y))
        visit[y][x] = True
        while q:
            cx, cy = q.pop()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = cx + dx
                ny = cy + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if land[ny][nx] == 1 and visit[ny][nx] == False:
                        min_x = min(min_x, nx)
                        max_x = max(max_x, nx)
                        visit[ny][nx] = True
                        size += 1
                        q.append((nx, ny))
        
        # for y in range(n):
        #     for x in range(m):
        #         if visit[y][x] == True and graph[y][x] == 0:
        #             graph[y][x] = size
    
        for x in range(min_x, max_x+1):
            result[x] += size
    
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and visit[y][x] == 0:
                tot_oil(x, y)
    
    def debug(graph):
        for l in graph:
            print(l)
    
    # print(result)
    return max(result)