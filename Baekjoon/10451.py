############ 1. DFS 풀이
# import sys
# from collections import deque
#
# read = sys.stdin.readline
#
# T = int(read().rstrip())
# for t in range(T):
#     N = int(read().rstrip())
#     arr = [0] + list(map(int, read().rstrip().split()))
#     visited = [0] * (N + 1)
#
#     def dfs(x):
#         visited[x] = 1
#         next = arr[x]
#         if visited[next] == 0:
#             dfs(next)
#     answer = 0
#     for i in range(1, N+1):
#         if visited[i] == 0:
#             dfs(i)
#             answer += 1
#     print(answer)

############ 2. BFS 풀이
# import sys
# from collections import deque
#
# read = sys.stdin.readline
#
# T = int(read().rstrip())
# for t in range(T):
#     N = int(read().rstrip())
#     arr = [0] + list(map(int, read().rstrip().split()))
#     visit = [0] * (N+1)
#
#     def bfs(x):
#         q = deque()
#         visit[x] = 1
#         q.append(arr[x])
#         while q:
#             n = q.popleft()
#             if visit[n] == 0:
#                 visit[n] = 1
#                 q.append(arr[n])
#     answer = 0
#     for i in range(1, N+1):
#         if visit[i] == 0:
#             answer += 1
#             bfs(i)
#     print(answer)