import sys
from collections import deque

read = sys.stdin.readline
N = int(input())

W = []
for _ in range(N):
    W.append(str(read().rstrip()))

cnt = 0
for i in W:
    H = deque()
    group = True
    for j in i:
        if not H:
            H.append(j)
            continue
        before = H.pop()
        # 이전에 나온적이 없거나, 직전에 나온 것이어야함
        if j not in H:
            H.append(before)
            H.append(j)
        else:
            if before == j:
                H.append(before)
            else:  # group 단어가 아님
                group = False
                break
    if group:
        cnt += 1

print(cnt)