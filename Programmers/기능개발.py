from collections import deque

def solution(progresses, speeds):
    answer = []
    
    num_works = len(progresses)
    Q = deque()
    for i in range(num_works):
        progress_left = 100 - progresses[i]
        if progress_left % speeds[i] == 0:
            Q.append(progress_left // speeds[i])
        else:
            Q.append(progress_left // speeds[i] + 1)
    
    print(Q)
    
    cur_date = 0
    while Q:
        date = Q.popleft()
        cur_date += date
        cnt = 1
        while Q:
            next_work = Q.popleft()
            if next_work <= cur_date:
                cnt += 1
            else:
                Q.appendleft(next_work - cur_date)
                break
        answer.append(cnt)
        
    return answer