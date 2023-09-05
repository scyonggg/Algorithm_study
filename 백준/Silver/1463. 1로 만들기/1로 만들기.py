import sys

read = sys.stdin.readline

n = int(read().rstrip())

d = [0] * (n+1)  # d[i] : i가 1이 될 때까지 걸리는 횟수
d[1] = 0
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
print(d[n])