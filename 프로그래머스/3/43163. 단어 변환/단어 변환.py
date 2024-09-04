from collections import deque
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    n = len(begin)
    w = len(words)
    visit = [0] * w
    
    q = deque()
    q.append((begin, 0))
    while q:
        cur, cnt = q.popleft()
        if cur == target:
            return cnt
        for idx, word in enumerate(words):
            diff_cnt = 0
            for length in range(len(word)):
                if cur[length] != word[length]:
                    diff_cnt += 1
            if diff_cnt == 1:
                visit[idx] = 1
                q.append((word, cnt + 1))
            
    return 0






"""
from collections import deque

def solution(begin, target, words):
    answer = 0
    
    num_words = len(words)
    len_word = len(begin)
    visit = [0] * num_words
    
    q = deque()
    q.append((begin, 0))

    while q:
        cur, cnt = q.popleft()
        if cur == target:
            answer = cnt
            break
        for idx, word in enumerate(words):
            if visit[idx] != 0:
                continue
            diff_cnt = 0
            for i in range(len_word):
                if cur[i] != word[i]:
                    diff_cnt += 1
            if diff_cnt == 1:
                visit[idx] = 1
                q.append((word, cnt + 1))
        
            
    
    return answer
"""