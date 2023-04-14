"""
값이 들어올 때마다 중간 값을 출력해야함.

Left heap과 Right heap이 있음.
Mid는 left heap에 속함.

case 1) 전체 수가 짝수일 때 새로운 값 num 입력
1-1) num <= mid
left heap에 num 삽입, 새로운 mid는 left heap.pop
1-2) num > mid
right heap에 num 삽입, 새로운 mid는 right heap.pop하여 left heap에 삽입

"""
# import sys
# import heapq
#
# read = sys.stdin.readline
# N = int(input())  # 입력할 수의 개수
#
# S = []  # 입력하는 정수
# heapL = []  # 중간값 mid보다 왼쪽 : max heap
# heapR = []  # 중간값 mid보다 오른쪽 : min heap
#
# for _ in range(N):
#     num = int(read().rstrip())
#     if len(heapL) == 0:
#         heapq.heappush(heapL, -(100000 + num))
#         print(num)
#         continue
#     mid = -heapq.heappop(heapL) - 100000
#
#     if num <= mid:
#         heapq.heappush(heapL, -(100000 + num))
#         heapq.heappush(heapL, -(100000 + mid))
#         if (len(heapL) + len(heapR)) % 2 == 0:
#             heapq.heappush(heapR, -heapq.heappop(heapL) - 100000)
#     elif num > mid:
#         heapq.heappush(heapR, num)
#         heapq.heappush(heapL, -(100000 + mid))
#         if (len(heapL) + len(heapR)) % 2 == 1:
#             heapq.heappush(heapL, -(100000 + heapq.heappop(heapR)))
#     else:
#         assert NotImplemented("Check")
#     mid = -heapq.heappop(heapL) - 100000
#     heapq.heappush(heapL, -(100000 + mid))
#     print(mid)

import sys
import heapq

read = sys.stdin.readline
N = int(input())  # 입력할 수의 개수

S = []  # 입력하는 정수
heapL = []  # 중간값 mid보다 왼쪽 : max heap
heapR = []  # 중간값 mid보다 오른쪽 : min heap

for _ in range(N):
    num = int(read().rstrip())
    if len(heapL) == 0:
        heapq.heappush(heapL, -num)
        print(num)
        continue
    mid = -heapq.heappop(heapL)

    if num <= mid:
        heapq.heappush(heapL, -num)
        heapq.heappush(heapL, -mid)
        if (len(heapL) + len(heapR)) % 2 == 0:
            heapq.heappush(heapR, -heapq.heappop(heapL))
    elif num > mid:
        heapq.heappush(heapR, num)
        heapq.heappush(heapL, -mid)
        if (len(heapL) + len(heapR)) % 2 == 1:
            heapq.heappush(heapL, -(heapq.heappop(heapR)))
    else:
        assert NotImplemented("Check")
    mid = -heapq.heappop(heapL)
    heapq.heappush(heapL, -mid)
    print(mid)
