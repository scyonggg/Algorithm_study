def solution(triangle):
    answer = 0
    h = len(triangle)
    dp = [[] for _ in range(h)]
    dp[0].append(triangle[0][0])
    
    for i in range(1, h):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i].append(dp[i-1][j] + triangle[i][j])
            elif j == len(triangle[i])-1:
                dp[i].append(dp[i-1][j-1] + triangle[i][j])
            else:
                dp[i].append(triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j]))
    answer = 0
    for val in dp[-1]:
        answer = max(answer, val)
    
    
    return answer