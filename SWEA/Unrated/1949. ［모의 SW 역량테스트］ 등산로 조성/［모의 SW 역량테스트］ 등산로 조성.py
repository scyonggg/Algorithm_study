"""
N : 3 ~ 8
K : 1 ~ 5
봉우리 높이 (board[r][c] 값): 1 ~ 20
가장 높은 봉우리 : 최대 5개
높이는 1보다 작을 수 있음. (정수)

"""
from collections import deque

def debug_3d(graphs, text: str=None):
    if text:
        print(text)
    for i in range(K+1):
        print(f'graphs[{i}]:')
        for r in range(N):
            for c in range(N):
                print(graphs[r][c][i], end=' ')
            print()
    return

def debug_2d(graph, text: str=None):
    if text:
        print(text)
    for g in graph:
        print(g)
    print()
    return

def find_highest_top():
    max_height = -1
    candidates = []
    for r in range(N):
        for c in range(N):
            height = maps[r][c]
            if max_height == height:
                candidates.append([r, c])
            elif max_height < height:
                max_height = height
                candidates = [[r, c]]
    return candidates, max_height

def check_visit(r, c, num, visit):
    for i in range(K+1):
        visit[r][c][i] = num
    return visit

def get_max_len(visit):
    max_len = -1
    for k in range(K+1):
        for r in range(N):
            for c in range(N):
                cur_len = visit[r][c][k]
                max_len = max(max_len, cur_len)
    return max_len

def bt(cr, cc, cpath, max_path, cflag, visit):
    """

    :param r: 현재 행
    :param c: 현재 열
    :param cpath: 현재까지 지나온 경로
    :param cflag: 현재까지 땅을 판 깊이.
    :param visit: 현재까지 방문한 위치 visit 배열
    :return: 현재까지 가장 긴 경로.
    """
    # 더 이상 산을 깎을 수 없고, 상하좌우 산이 현재보다 높거나 같으면 더 이상 진행 불가.
    cheight = maps[cr][cc]
    # debug_3d(visit, f'visit: ')
    if cflag != 0 and \
            (0 <= cr+1 < N and maps[cr+1][cc] >= cheight) and \
            (0 <= cr-1 < N and maps[cr-1][cc] >= cheight) and \
            (0 <= cc+1 < N and maps[cr][cc+1] >= cheight) and \
            (0 <= cc-1 < N and maps[cr][cc-1] >= cheight):
        return cpath if len(cpath) > len(max_path) else max_path
    # 산을 깎을 기회가 있더라도 cheight + K보다 상하좌우산이 높거나 같으면 더 이상 진행 불가
    if cflag == 0 and \
            (0 <= cr + 1 < N and maps[cr + 1][cc] >= cheight+K) and \
            (0 <= cr - 1 < N and maps[cr - 1][cc] >= cheight+K) and \
            (0 <= cc + 1 < N and maps[cr][cc + 1] >= cheight+K) and \
            (0 <= cc - 1 < N and maps[cr][cc - 1] >= cheight+K):
        return cpath if len(cpath) > len(max_path) else max_path

    for dr, dc in zip((0, 0, -1, 1), (-1, 1, 0, 0)):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < N:
            if cflag != 0:  # 산 깎기 기회 소진. 더 이상 산을 깎을 수 없음
                if visit[nr][nc][cflag] < visit[cr][cc][cflag] + 1 and maps[nr][nc] < maps[cr][cc]:  # 더 긴 경로가 있고, 현재보다 낮으면 방문 가능
                    tmp = visit[nr][nc][cflag]
                    visit[nr][nc][cflag] = visit[cr][cc][cflag] + 1
                    path = cpath + [[nr, nc]]
                    max_path = path if len(path) > len(max_path) else max_path
                    npath = bt(nr, nc, path, max_path, cflag, visit)
                    max_path = npath if len(npath) > len(max_path) else max_path
                    visit[nr][nc][cflag] = tmp
                    # visit[nr][nc][cflag] = 0
            else:  # 산 깎기 기회 남아있음.
                for k in range(K+1):  # 0부터 K까지 산을 깎을 수 있음.
                    if visit[nr][nc][0] == 0 and visit[nr][nc][k] < visit[cr][cc][cflag] + 1 and maps[nr][nc] - k < maps[cr][cc]:
                        tmp = visit[nr][nc][cflag]
                        visit[nr][nc][k] = visit[cr][cc][0] + 1
                        path = cpath + [[nr, nc]]
                        max_path = path if len(path) > len(max_path) else max_path
                        maps[nr][nc] -= k
                        npath = bt(nr, nc, path, max_path, k, visit)
                        max_path = npath if len(npath) > len(max_path) else max_path
                        maps[nr][nc] += k
                        visit[nr][nc][k] = tmp
    # 주변 모두 탐색 완료
    return max_path

def dfs(r, c):
    # visit[r][c][k] : k만큼 산을 깎은 상황의 visit 배열.
    visit = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    visit = check_visit(r, c, 1, visit)
    q = deque()
    q.append([r, c, 0])
    while q:
        cr, cc, cflag = q.popleft()  # cflag = 0 : 산 깎을 수 있음.  X : X만큼 산을 깎은 상태.
        for dr, dc in zip((0, 0, -1, 1), (-1, 1, 0, 0)):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                if cflag != 0:  # 산 깎기 기회 소진. 더 이상 산을 깎을 수 없음.
                    if visit[nr][nc][cflag] == 0 and maps[nr][nc] < maps[cr][cc]:
                        visit[nr][nc][cflag] = visit[cr][cc][cflag] + 1
                else:  # 산 깎기 기회 남아있음. 0 ~ K 만큼 산을 깎은 경우를 고려.
                    for i in range(K+1):
                        if visit[nr][nc][i] == 0 and maps[nr][nc] - i < maps[cr][cc]:  # i만큼 산을 깎은 결과
                            visit[nr][nc][i] = visit[cr][cc][0] + 1
                            q.append([nr, nc, i])
    # debug_3d(visit)
    max_len = get_max_len(visit)
    # for i in range(K):
    #    debug_3d(visit, i, f'visit[{i}]:')
    return max_len

def find_climbing_path(candidate):
    r, c = candidate
    visit = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    visit = check_visit(r, c, 1, visit)
    return bt(r, c, [[r, c]], [[r, c]], 0, visit)

def main():
    # 1. 가장 높은 봉우리들 찾기
    candidates, max_height = find_highest_top()
    # 각 봉우리들에 대해 등산로 탐색. 가장 긴 등산로 찾기
    max_len = -1
    for candidate in candidates:
        cand_path = find_climbing_path(candidate)
        max_len = max(max_len, len(cand_path))

    return max_len

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        maps = [list(map(int, input().split())) for _ in range(N)]
        ans = main()
        print(f'#{t+1} {ans}')
        # if t == 3:
        #     ans = main()
        #     print(f'#{t+1} {ans}')
        #     break
