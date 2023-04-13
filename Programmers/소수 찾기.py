'''Note
1. numbers로 만들 수 있는 모든 숫자들 조합해보기.
2. 소수 판별하는 코드 작성.
'''
from collections import deque
import math
def solution(numbers):
    answer = 0
        
    # 1. 만들 수 있는 모든 숫자들 조합 : ret

    def dfs(cnt, num_str, k):
        nonlocal ret, numbers, stack, used
        if cnt == k:
            num_str = ''.join(stack)
            ret.append(int(num_str))
            return
        
        for i in range(len(numbers)):
            if used[i] == False:
                stack.append(numbers[i])
                used[i] = True
                dfs(cnt + 1, num_str, k)
                used[i] = False
                stack.pop()
        return
    
    ret = []
    for k in range(1, len(numbers) + 1):
        stack = deque()
        used = [False] * len(numbers)
        dfs(0, '', k)
    
    ret = list(set(ret))    
    
    if 0 in ret:
        ret.remove(0)
    if 1 in ret:
        ret.remove(1)
    
    print(ret)
    
    # 2. 소수 판별하는 함수
    def sosu(num_list: list):
        nonlocal answer
        for i in num_list:
            det = True
            for j in range(2, math.floor(math.sqrt(i))+1):
                if i % j == 0:
                    det = False
            if det:
                answer += 1
    
    sosu(ret)
    return answer