'''Node
< 문제 조건 >
N행 4열
바로 아래 칸으로는 이동할 수 없다.

< 생각 >
아래서부터 위로 올라간다면?
'''
def solution(land):
    answer = 0

    for row in range(1, len(land)):
        land[row][0] += max(land[row-1][1], land[row-1][2], land[row-1][3])
        land[row][1] += max(land[row-1][0], land[row-1][2], land[row-1][3])
        land[row][2] += max(land[row-1][1], land[row-1][0], land[row-1][3])
        land[row][3] += max(land[row-1][1], land[row-1][2], land[row-1][0])
    
    return max(land[-1])