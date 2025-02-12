"""

"""
import math

def solution(money):
    answer = 0
    N = len(money)  # 3 <= N <= 1e6
        
    # 0 ~ N-2까지 탐색
    dp = [0 for i in range(N)]
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, N-1):
        dp[i] = max(dp[i-1], money[i] + dp[i-2])
    answer = max(dp)
    
    # 1 ~ N-1까지 탐색
    dp = [0 for i in range(N)]
    dp[0] = 0
    dp[1] = money[1]
    
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    answer = max(max(dp), answer)
    return answer