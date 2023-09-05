'''
n번째 계단에 올라오는 경우
1. n-1번째 계단
    dp[n] = dp[n-3] + stairs[n-1] + stairs[n]
2. n-2번째 계단
    dp[n] = dp[n-2] + stairs[n]

dp[n] : n번째 계단까지 올라왔을 때 얻을 수 있는 최대값
dp[n] = max(n-1번째 계단에서 올라온 경우의 최대값, n-2번째 계단에서 올라온 경우의 최대값)
dp[n] = max(dp[n-3] + stairs[n-1] + stairs[n], dp[n-2] + stairs[n])

'''
import sys
read = sys.stdin.readline

h = int(read().rstrip())
stairs = [0]
for _ in range(h):
    stair = int(read().rstrip())
    stairs.append(stair)

if h == 1:
    print(stairs[1])
    exit(0)
elif h == 2:
    print(max(stairs[2], stairs[1]+stairs[2]))
    exit(0)

if True:
    dp = [0] * (h+1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, h+1):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
    print(dp[-1])