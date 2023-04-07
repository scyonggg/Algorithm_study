import sys

read = sys.stdin.readline
N = int(input())
M = []  # 회의 시간표
for i in range(N):
    M.append(list(map(int, read().rstrip().split())))

M.sort(key=lambda x: x[0])  # 시작 순서가 빠른 순서대로 정렬
M.sort(key=lambda x: x[1])  # 종료 시간이 빠른 순서대로 정렬

cnt = 1
cur = M[0][1]
for i in range(1, N):
    if M[i][0] >= cur:
        cur = M[i][1]
        cnt += 1
print(cnt)