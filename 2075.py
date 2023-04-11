import sys
import heapq

read = sys.stdin.readline
N = int(input())
P = []
for _ in range(N):
    data = list(map(int, read().rstrip().split()))
    for i in data:
        if len(P) < N:
            heapq.heappush(P, i)
        else:  # 가장 큰 N개만 담는다
            num = heapq.heappop(P)  # 우선순위 큐에서 가장 작은 값.
            if i < num:  # 더 작은 값은 넣을 필요 없음
                heapq.heappush(P, num)
            else:
                heapq.heappush(P, i)

print(heapq.heappop(P))