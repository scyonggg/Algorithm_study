n = int(input())
ans = 0
row = [0] * n

def is_avail(x):  # x번째 row에 퀸을 놓을 수 있는가?
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):  # 열이 같거나 대각선이 같으면 안됨
            return False
    return True

def dfs(x):  # x번째 row에 퀸 놓기
    global ans

    if x == n:
        ans += 1
    else:  # row마다 퀸 하나씩 놓기
        for i in range(n):  # 퀸을 놓을 col 번호 찾기
            row[x] = i
            if is_avail(x):
                dfs(x+1)

dfs(0)
print(ans)