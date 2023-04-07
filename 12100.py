import sys
from copy import deepcopy

N = int(input())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ans = 0
# board[i][j]
def up(board):
    for j in range(N):  # row 방향
        pointer = 0
        for i in range(1, N):  # col 방향
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:  # pointer가 가리키는 수가 0 -> tmp를 pointer 위치로 이동
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp:  # pointer가 가리키는 수가 현재 위치와 일치
                    board[pointer][j] = tmp * 2
                    pointer += 1
                else:  # pointer가 가리키는 수가 현재 위치와 다를 때
                    pointer += 1
                    board[pointer][j] = tmp
    return board

def down(board):
    for j in range(N):  # row 방향 탐색
        pointer = N-1
        # for i in reversed(range(N-1)):  # col 방향 탐색 N-2, ...
        for i in range(N-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:  # pointer가 가리키는 수가 0 -> tmp를 pointer 위치로 이동
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp:  # pointer가 가리키는 수가 일치
                    board[pointer][j] = tmp * 2
                    pointer -= 1
                else:  # pointer가 가리키는 수가 일치하지 않음
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

def left(board):
    for i in range(N):  # col 방향 탐색
        pointer = 0
        for j in range(1, N):  # row 방향
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:  # pointer가 가리키는 수가 0 -> tmp를 pointer로 이동
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:  # 현재 숫자 = pointer 숫자 -> pointer에 2배 저장
                    board[i][pointer] = tmp * 2
                    pointer += 1
                else:  # 현재 숫자와 pointer 숫자가 다른 경우
                    pointer += 1
                    board[i][pointer] = tmp
    return board

def right(board):
    for i in range(N):  # col 방향 탐색
        pointer = N - 1
        # for j in reversed(range(N-1)):  # row 방향 탐색
        for j in range(N-2, -1, -1):  # row 방향 탐색
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:  # pointer가 가리키는 수가 0
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] = tmp * 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board

def dfs(cnt, arr):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        copy_arr = deepcopy(arr)
        if i == 0:
            dfs(cnt+1, up(copy_arr))
        elif i == 1:
            dfs(cnt+1, down(copy_arr))
        elif i == 2:
            dfs(cnt+1, left(copy_arr))
        elif i == 3:
            dfs(cnt+1, right(copy_arr))

dfs(0, board)
print(ans)