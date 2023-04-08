"""
보석 개수 : N개
보석 한 개마다 무게 M, 가격 V가 있음.
가방 개수 : K개, 최대 무게 C
가방 하나에 보석 하나밖에. -> 선택할 보석 개수 = K

생각 1.
    - 가방을 최소 무게 순으로 정렬 -> queue에 넣는다.
    - 보석은 가벼운 순서대로 정렬, 같은 무게라면 비싼 것 순서대로
    - queue에서 가방을 꺼내면서, 넣을 수 있는 보석 중에 가장 비싼것 넣기


"""

import sys
import heapq

read = sys.stdin.readline
N, K = map(int, input().split())

B = []  # 보석. B[x][0]: 무게, B[x][1]: 가격. len(B) = N
for _ in range(N):
    # B.append(list(map(int, read().rstrip().split())))
    heapq.heappush(B, list(map(int, read().rstrip().split())))

G = [int(read().rstrip()) for _ in range(K)]  # 가방. G[x]: 무게 len(G) = K
G.sort()

ans = 0
tmp_B = []
for g in G:
    while B and g >= B[0][0]:  # 작은 보석도 못담으면 아무것도 못담는다.
        heapq.heappush(tmp_B, -heapq.heappop(B)[1])  # 보석의 무게는 최대 힙으로 정렬
    if tmp_B:  # 담을 수 있는 보석이 있을 경우
        ans -= heapq.heappop(tmp_B)
    elif not B:
        break
print(ans)