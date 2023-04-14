import sys

sys.setrecursionlimit(100000)
read = sys.stdin.readline
N = int(read().rstrip())  # 센서 개수
K = int(read().rstrip())  # 집중국 개수
S = sorted(list(map(int, read().rstrip().split())), reverse=True)  # 센서 좌표

def solution():
    if N <= K:
        print(0)
        return
    else:
        dist = []
        u = S[0]
        for i in S[1:]:
            dist.append(u-i)
            u = i
        dist.sort(reverse=True)
        print(sum(dist[K-1:]))
        return
solution()