'''
n=1 : 1
n=2 : 2
n=3 : 4
n=4 : 1+3, 2+2, 3+1
n=5 : 2+3, 3+2, 4+1

dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
'''

import sys
read = sys.stdin.readline
T = int(read().rstrip())
for _ in range(T):
    n = int(read().rstrip())
    dp = [0] * (n+1)
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])