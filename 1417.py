import sys
import heapq

read = sys.stdin.readline

N = int(input())

V = []
for i in range(N):
    data = int(read().rstrip())
    if i == 0:
        D = data
        continue
    V.append(-data)

heapq.heapify(V)  # 다솜의 득표수는 힙에 없다.

cnt = 0
while True:
    if len(V) == 0:
        print(0)
        break
    vote1 = -heapq.heappop(V)  # 현재 1등 득표수
    if D + cnt > vote1:
        print(cnt)
        break
    heapq.heappush(V, -(vote1-1))
    cnt += 1
