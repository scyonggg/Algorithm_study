'''
<문제>
- 구명보트는 2명까지.
- 최대한 적은 개수
- len(people) : 1 ~ 50,000
- people : 40 ~ 240
- limit : 40 ~ 240
- limit > max(people)


'''
from collections import deque
def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    deq = deque(people)
    
    while deq:  # 구출해야 할 사람이 없을 때까지 반복
        if len(deq) == 1:  # 마지막 한명은 보트 혼자 탄다
            answer += 1
            return answer
        
        max_weight = deq.popleft()
        min_weight = deq.pop()
        if max_weight + min_weight <= limit:
            answer += 1
        else:  # max_weight는 무조건 보트를 혼자 타야한다.
            deq.append(min_weight)
            answer += 1
    
    return answer