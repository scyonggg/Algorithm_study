"""
Note
P[][0], P[][1]
P[][0]을 루트로하는 힙 만들기.
1~N까지 돌면서 각 숫자에 힙이 있으면 그 문제들을 먼저 풀것. 단, 그 힙은 min heap

<e.g.>
N = 9   1 2 3 4 5 6 7 8 9
8 3
4 1
6 9
7 3
5 4
3 1
->
x   2   x   x   5   x   7   8   9
0   0   1   1   4   0   3   3   6
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0

"""
import sys
import heapq

read = sys.stdin.readline
N, M = map(int, read().rstrip().split())

ans = []
G = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
Q = []
for _ in range(M):
    start, end = map(int, read().rstrip().split())
    G[start].append(end)
    inDegree[end] += 1

for i in range(1, N+1):
    if inDegree[i] == 0:  # in_degree가 없으면 우선순위 큐에 넣는다.
        heapq.heappush(Q, i)

while Q:
    p = heapq.heappop(Q)
    ans.append(p)
    for i in G[p]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(Q, i)

for i in ans:
    print(i, end=' ')