import heapq

def solution(operations):
    answer = []
    
    max_pq = []
    min_pq = []
    
    for operation in operations:
        inst, data = operation.split()
        if data.startswith('-'):
            num = int(data[1:]) * -1
        else:
            num = int(data)
            
        if inst == 'I':
            heapq.heappush(min_pq, num)
            heapq.heappush(max_pq, -num)
        elif inst == 'D':
            if len(max_pq) == 0:
                continue
            if num == 1:
                max_num = heapq.heappop(max_pq)
                min_pq.remove(-max_num)
            elif num == -1:
                min_num = heapq.heappop(min_pq)
                max_pq.remove(-min_num)
    return [-heapq.heappop(max_pq), heapq.heappop(min_pq)] if len(max_pq) != 0 else [0, 0]