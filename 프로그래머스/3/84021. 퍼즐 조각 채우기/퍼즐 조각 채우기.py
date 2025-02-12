from collections import deque

def debug(graph):
    for g in graph:
        print(g)
    print()
    
def rotate(graph):
    """
    1 2 3 4
    5 6 7 8
    
    5 1
    6 2
    7 3
    8 4
    """
    R = len(graph)
    C = len(graph[0])
    rotated = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            rotated[c][R-r-1] = graph[r][c]
    return rotated

def bfs(x, y, board, visited, t):
    # x : 행, y : 열
    # t = 0 : 빈칸, 1 : 퍼즐
    R = len(board)
    C = len(board[0])
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    path = []
    while q:
        cx, cy = q.popleft()
        path.append([cx, cy])
        for dx, dy in zip((-1, 1, 0, 0), (0, 0, 1, -1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny] == t:
                q.append((nx, ny))
                visited[nx][ny] = True
    return path 

def path_to_graph(path):
    new_boards = []
    for p in path:
        min_x, min_y = 9999, 9999
        max_x, max_y = -1, -1
        for x, y in p:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        new_board = [[0] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
    
        for x, y in p:
            cx = x - min_x
            cy = y - min_y
            new_board[cx][cy] = 1
        new_boards.append(new_board)
    return new_boards

def is_same_board(board1, board2):
    R1 = len(board1)
    C1 = len(board1[0])
    R2 = len(board2)
    C2 = len(board2[0])
    if R1 != R2 or C1 != C2:
        return False
    for r in range(R1):
        for c in range(C1):
            if board1[r][c] != board2[r][c]:
                return False
    return True

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    # rotated = rotate(game_board)  # RxC 크기의 board를 90도 회전
    
    visited = [[False] * N for _ in range(N)]
    tot_blanks = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and game_board[i][j] == 0:
                blanks = bfs(i, j, game_board, visited, 0)  # game_board에서 0인 좌표들의 그룹
                tot_blanks.append(blanks)
    tot_blanks_graph = path_to_graph(tot_blanks)  # game_board에서 0인 좌표들의 그룹을 다시 graph로 만듦.
    
    # print('blanks in game_board')
    # for blanks, graphs in zip(tot_blanks, tot_blanks_graph):
    #     print(blanks, end='\n')
    #     debug(graphs)
    
    visited = [[False] * N for _ in range(N)]
    tot_puzzles = []
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and table[r][c] == 1:
                puzzle_path = bfs(r, c, table, visited, 1)  # table에서 1인 좌표들의 그룹
                tot_puzzles.append(puzzle_path)
    tot_puzzles_graph = path_to_graph(tot_puzzles)  # table에서 1인 좌표들의 그룹을 다시 graph로 만듦.
    # print('puzzles in table')
    # for puzzle, graph in zip(tot_puzzles, tot_puzzles_graph):
    #     print(puzzle)
    #     debug(graph)
        
    available_puzzles = {k: True for k in range(len(tot_puzzles))}
    for idx, blank in enumerate(tot_blanks):  # game_board의 빈칸 그룹 탐색
        is_same = False
        for ii, puzzle in enumerate(tot_puzzles):  # table의 퍼즐 그룹 탐색
            if not available_puzzles[ii]:
                continue
            if len(blank) == len(puzzle):  # 빈칸 그룹과 퍼즐 그룹 개수가 같을 경우
                blank_graph = tot_blanks_graph[idx]
                puzzle_graph = tot_puzzles_graph[ii]
                for _ in range(4):
                    puzzle_graph = rotate(puzzle_graph)
                    is_same = is_same_board(blank_graph, puzzle_graph)
                    if is_same:
                        break
                if is_same:
                    available_puzzles[ii] = False
                    break
        if is_same:
            answer += len(puzzle)
            
    return answer