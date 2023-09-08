'''
X분동안 각 심사관들이 심사할 수 있는 사람 수의 합이 n이상 될때까지.
'''
from collections import deque

def solution(n, times):
    answer = 0
    times.sort()
    
    left = times[0]
    right = times[-1] * n
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break
        
        if cnt >= n:
            answer = mid
            right = mid - 1
        elif cnt < n:
            left = mid + 1
    
    return answer