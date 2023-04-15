'''Note
제거할 수 있는 수의 개수가 k개
topk = number[:k]
max_topk = max(topk)

< sol 1 > 재귀는 시간 초과.
1) max_topk가 k+1보다 작다면 -> topk 다 지우기
2) max_topk가 k+1보다 크다면 -> k를 k-1개로 줄여서 반복?

< sol 2> 스택 이용
stack 크기가 k가 될때까지 반복
-> 마지막에 들어온 원소보다 큰 원소가 들어와야.
'''
from collections import deque
def solution(number, k):
    q = deque()
    stack = deque()
    
    for i in number:
        q.append(i)
    
    while q and k:  # 아직 제거해야할 숫자가 남았다.
        while stack and stack[-1] < q[0]:  # 다음 숫자보다 작으면 버린다.
            stack.pop()
            k -= 1
            if k == 0:
                break
        stack.append(q.popleft())
    
    # k가 남았는데 number가 끝까지 돌았을 경우
    while k and stack:
        stack.pop()
        k -= 1
        
    return ''.join(stack+q)