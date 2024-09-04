def solution(skill, skill_trees):
    answer = 0
    
    avail = [None] * len(skill)
    cur = -1
    for s in skill:
        cur += 1
        if cur > 0:
            avail[cur] = avail[cur-1] + s
        else:
            avail[cur] = s
    print(avail)
    
    for skill_tree in skill_trees:
        _tree = ""
        for s in skill_tree:
            if s in skill:
                _tree += s
        print(_tree)
        if _tree in avail or _tree == "":
            answer += 1
            
    return answer