def solution(board, skill):
    answer = 0
    
    n = len(board)
    m = len(board[0])
    
    palette = [[0] * (m+1) for _ in range(n+1)]
    
    for s in skill:
        _type, _r1, _c1, _r2, _c2, _degree = s
        if _type == 1:  # 공격
            palette[_r1][_c1] -= _degree
            palette[_r1][_c2+1] += _degree
            
            palette[_r2+1][_c1] += _degree
            palette[_r2+1][_c2+1] -= _degree
            
        elif _type == 2:  # 수비
            palette[_r1][_c1] += _degree
            palette[_r1][_c2+1] -= _degree
            
            palette[_r2+1][_c1] -= _degree
            palette[_r2+1][_c2+1] += _degree
            
    # print(palette)
    for row in range(n):
        for col in range(m):
            palette[row][col+1] += palette[row][col]
        
    for col in range(m):
        for row in range(n):
            palette[row+1][col] += palette[row][col]
        
    # print(palette)

    for row in range(n):
        for col in range(m):
            board[row][col] += palette[row][col]
            if board[row][col] > 0:
                answer += 1
    # print(board)
    return answer