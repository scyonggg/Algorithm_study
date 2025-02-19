

def solution(N, heights):
    """
    4 <= N <= 1000
    0 <= heights_i <= 255
    """
    ans = 0
    for n in range(2, N-2):  # 0, 1, N-2, N-1 번째 건물의 높이는 0이므로 제외. O(N)
        max_h = -1
        for m in range(n-2, n+3):  # n-2, n-1, n, n+1, n+2 까지 탐색. O(1)
            if m == n:
                continue
            h = heights[m]
            max_h = max(h, max_h)
        cnt = heights[n] - max_h
        if cnt > 0:
            ans += cnt
    return ans

def main():
    for testcase in range(10):
        N = int(input())  # 건물의 개수
        heights = list(map(int, input().split()))
        print(f'#{testcase+1} {solution(N, heights)}')

if __name__ == '__main__':
    main()