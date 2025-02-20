from collections import deque

def debug_2d(graph):
    for g in graph:
        print(g)
    print()
    return


def solution(N, graph):
    def update_dp():
        nonlocal max_log, children, dp, depth
        N = len(dp) - 1
        for k in range(1, max_log):
            for i in range(1, N + 1):
                dp[i][k] = dp[dp[i][k - 1]][k - 1]
        return

    def get_lca(u, v):
        nonlocal max_log, dp, depth
        if depth[u] < depth[v]:  # 항상 u가 v보다 깊도록.
            u, v = v, u

        for k in range(max_log - 1, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:  # 같은 높이로 맞춤.
                u = dp[u][k]

        if u == v:
            return u

        for i in range(max_log - 1, -1, -1):
            if dp[u][i] != dp[v][i]:
                u = dp[u][i]
                v = dp[v][i]

        return dp[v][0]

    def bfs():
        nonlocal max_log, children, dp, depth

        q = deque()
        q.append(1)  # 번호, 깊이
        depth[1] = 0
        while q:
            cn = q.popleft()
            for child in children[cn]:
                depth[child] = depth[cn] + 1
                q.append(child)
        return

    """
    N : 노드 개수
    """
    ans = 0
    if N == 1:
        return ans

    max_log = 17
    # max_log = math.ceil(math.log2(pow(10, 5))) + 1
    children = [[] for _ in range(N+1)]
    dp = [[0] * max_log for _ in range(N+1)]  # dp[i][j] : i번 노드의 2^j번째 윗 부모
    depth = [-1 for _ in range(N+1)]

    for i, g in enumerate(graph):
        dp[i+2][0] = g
        children[g].append(i+2)

    bfs()
    update_dp()

    q = deque([1])
    prev = 1
    while q:
        c = q.popleft()
        lca = get_lca(prev, c)
        # ans += abs(depth[prev] - depth[lca]) + abs(depth[c] - depth[lca])
        ans += depth[prev] + depth[c] - 2 * depth[lca]
        prev = c
        for child in children[c]:
            q.append(child)

    return ans

def main():
    T = int(input())  # 테스트 케이스 수
    # for t in range(1):
    for t in range(T):
        N = int(input())  # 자연수, 1 <= N <= 100,000
        graph = list(map(int, input().split()))  # 각 노드의 부모 정점
        print(f'#{t+1} {solution(N, graph)}')

if __name__ == '__main__':
    main()