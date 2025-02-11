"""
max_dp[i][j] : i부터 j까지 연산 최댓값
min_dp[i][j] : i부터 j까지 연산 최솟값
1 2 3 4 5  ->  N = 5
(1) (2 3 4 5)
(1 2) (3 4 5)
(1 2 3) (4 5)
(1 2 3 4) (5)
"""
import math

def debug(graph):
    for g in graph:
        print(g)
    print()
    
def solution(arr):
    answer = -1
    N = (len(arr) + 1) // 2
    min_dp = [[math.inf] * N for _ in range(N)]
    max_dp = [[-math.inf] * N for _ in range(N)]
    
    for i in range(N):
        min_dp[i][i] = int(arr[i*2])
        max_dp[i][i] = int(arr[i*2])
    
    for c in range(1, N):  # 괄호 묶음의 숫자 개수
        for i in range(N-c):
            j = i + c
            for k in range(i, j):  # i부터 j(i+c)까지 
                if arr[k*2 + 1] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                elif arr[k*2 + 1] == "-":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
            # debug(max_dp)
    return max_dp[0][-1]
        
    return answer

# 5 - 3 + 1 + 2 - 4