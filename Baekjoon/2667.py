import sys
from collections import deque, Counter

sys.setrecursionlimit(10000000)
read = sys.stdin.readline
N = int(input())

arr = []
for i in range(N):
    line = list(map(int, read().rstrip()))
    arr.append(line)

visit = [[0] * N for _ in range(N)]
def dfs(x, y, ans):
    visit[y][x] = ans

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx = dx + x
        ny = dy + y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[ny][nx] == 1 and visit[ny][nx] == 0:
            dfs(nx, ny, ans)

ans = 0
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1 and visit[y][x] == 0:
            ans += 1
            dfs(x, y, ans)

print(ans)

cnt = [0] * (ans + 1)
for y in range(N):
    for x in range(N):
        if visit[y][x] != 0:
            cnt[visit[y][x]] += 1

cnt.sort()
for i in range(1, len(cnt)):
    print(cnt[i])



# def bfs(x, y, idx):
#     q = deque()
#     visit[y][x] = idx
#     q.append((x, y))
#     while q:
#         cx, cy = q.popleft()
#         for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             nx = dx + cx
#             ny = dy + cy
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue
#             if arr[ny][nx] == 1 and visit[ny][nx] == 0:
#                 visit[ny][nx] = idx
#                 q.append((nx, ny))
#
# answer = 0
# for y in range(N):
#     for x in range(N):
#         if visit[y][x] == 0:
#             answer += 1
#             bfs(x, y, answer)
#
# print(visit)