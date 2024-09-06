def solution(targets):
    """
    1 <= len(targets) <= 500,000
    """
    answer = 0
    sorted_target = sorted(targets, key=lambda x: [x[1], x[0]])

    cur = 0
    
    for target in sorted_target:
        s = target[0]
        
        if cur <= s:
            cur = target[1]
            answer += 1
        
    return answer