import sys
from collections import deque

sys.setrecursionlimit(1000000)
read = sys.stdin.readline

n = int(read().rstrip())

maximum = 0
graph = []
for i in range(n):
    data = list(map(int, read().rstrip().split()))
    graph.append(data)
    for l in range(len(data)):
        if data[l] > maximum:
            maximum = data[l]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, graph, visited):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[y][x] <= 0:
        return False

    if graph[y][x] > 0:
        if visited[y][x] == False:
            visited[y][x] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny, graph, visited)
            return True
        else:
            return False
    return False


best = 0
for h in range(maximum):
    visited = [[False] * n for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, graph, visited) == True:
                answer += 1
    if answer > best:
        best = answer
    for i in range(n):
        for j in range(n):
            graph[i][j] -= 1

print(best)
