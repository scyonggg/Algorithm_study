from collections import deque
def solution(begin, target, words):
    answer = 0
    
    n = len(begin)  # 글자 수
    m = len(words)  # words 개수
    
    Q = deque()
    Q.append([begin, 0])
    visit = [False] * len(words)
    
    while Q:
        cword, cnt = Q.popleft()
        if cword == target:
            answer = cnt
            break
        for idx, j in enumerate(words):  # words와 비교
            tmp_cnt = 0
            for i in range(n):  # 각 글자마다 바꿀 수 있는지 황긴
                if visit[idx] == False:
                    if cword[i] != j[i]:  # 글자가 다른 경우
                        tmp_cnt += 1
            if tmp_cnt == 1:  # 다른 글자가 하나밖에 없을 경우
                visit[idx] = True
                Q.append([j, cnt+1])
    
    return answer