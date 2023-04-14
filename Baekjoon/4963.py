import sys

read = sys.stdin.readline
sys.setrecursionlimit(10000)
while True:
    w, h = map(int, read().rstrip().split())
    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, read().rstrip().split())))

    def dfs(x, y):
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    dfs(x+i, y+j)
            return True
        return False

    result = 0
    for i in range(w):
        for j in range(h):
            if dfs(i, j) == True:
                result += 1
    print(result)
