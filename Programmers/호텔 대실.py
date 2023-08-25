from heapq import heappush, heappop, heapify


def solution(book_time):
    answer = 1

    book_time_min = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_min.sort(key=lambda x: x[0])

    heap = []
    for start, end in book_time_min:
        if not heap:
            heappush(heap, end + 10)
            continue
        if heap[0] <= start:
            heappop(heap)
            heappush(heap, end + 10)
        else:
            answer += 1
            heappush(heap, end + 10)

    return answer