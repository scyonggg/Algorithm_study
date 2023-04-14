import sys
import heapq

read = sys.stdin.readline
N = int(input())

heap = []
ans = 0
for _ in range(N):
    data = int(read().rstrip())
    if data == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, data)