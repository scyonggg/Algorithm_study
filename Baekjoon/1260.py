import sys
from collections import deque

read = sys.stdin.readline

n, m, v = map(int, read().rstrip().split())
visited_bfs = [0] * (n+1)
visited_dfs = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]
for nm in range(m):
    x, y = map(int, read().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

def bfs(x):
    queue = deque()
    queue.append(x)
    visited_bfs[x] = 1
    while queue:
        nx = queue.popleft()
        print(nx, end=' ')
        for i in range(1, n+1):
            if visited_bfs[i] == 1:
                continue
            if graph[nx][i] == 1:
                visited_bfs[i] = 1
                queue.append(i)

def dfs(x):
    visited_dfs[x] = 1
    print(x, end=' ')
    for i in range(1, n+1):
        if visited_dfs[i] == 1:
            continue
        if graph[x][i] == 1:
            visited_dfs[i] = 1
            dfs(i)

dfs(v)
print()
bfs(v)
