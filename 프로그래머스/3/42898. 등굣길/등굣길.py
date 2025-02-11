"""
(x, y)
m : 열 (y), n : 행 (x)
"""

def debug(graph):
    for g in graph:
        print(g)
    print()

def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] not in puddles:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
    answer = dp[n][m]
    return answer % 1_000_000_007