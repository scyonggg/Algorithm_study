import sys
import heapq

read = sys.stdin.readline
N = int(input())

card = sorted(int(read().rstrip()) for _ in range(N))
heapq.heapify(card)
res = 0
while len(card) > 1:
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    heapq.heappush(card, x+y)
    res += x+y
print(res)