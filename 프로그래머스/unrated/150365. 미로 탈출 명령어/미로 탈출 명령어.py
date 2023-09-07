import sys
sys.setrecursionlimit(1000000)
def solution(n, m, x, y, r, c, k):
    answer = ''
    
    direction = ['d', 'l', 'r', 'u']
    flag = False
    
    def dfs(cx, cy, move, way):
        nonlocal flag, answer, direction
        if flag == True:
            return
                
        if flag == False and cx == r and cy == c and move == k:
            answer = way
            flag = True
            return
        
        if move == k:
            return

        if abs(r - cx) + abs(c - cy) > k - move:
            return
        
        for idx, (dx, dy) in enumerate(((1, 0), (0, -1), (0, 1), (-1, 0))):
            if flag == True:
                return
            
            
            nx = cx + dx
            ny = cy + dy
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            dfs(nx, ny, move + 1, way + direction[idx])
    
    if (abs(r-x) + abs(c-y) - k) % 2 != 0 or (abs(r-x) + abs(c-y)) > k:
        return 'impossible'
    
    dfs(x, y, 0, '')
    
    return answer