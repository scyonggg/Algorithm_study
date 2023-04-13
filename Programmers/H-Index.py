
def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    if len(citations) == 1:
        return 0
    
    for i in range(len(citations)-1):
        h = i+1  # cited번 이상 인용된 논문들의 개수
        if citations[i] >= h and citations[i+1] <= h:
            answer = h
    
    if citations[-1] > len(citations):
        answer = len(citations)
    
    
    return answer