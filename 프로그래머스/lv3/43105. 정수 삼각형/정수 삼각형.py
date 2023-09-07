'''
삼각형의 높이 : h = len(triangle)
len(triangle[i]) = i+1
i번째 level의 원소 j를 가정
if j != 0:
    T_ij = max(T_(i-1)(j-1), T_(i-1)j)
elif j == 0:
    T_ij = T_(i-1)j
'''
def solution(triangle):
    answer = 0
    
    h = len(triangle)
    ans = [0] * h
    s = 0
    for i in range(1, h):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])
    