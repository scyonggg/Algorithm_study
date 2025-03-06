def solution(info, edges):
    answer = 0
    
    visit = [False] * len(info)
    diff = [1, 0]
    
    def dfs(sheeps, wolves, maxi):
        if sheeps > wolves:
            maxi = max(sheeps, maxi)
        else:
            return maxi
        
        for p, c in edges:
            if visit[p] and not visit[c]:
                visit[c] = True
                if info[c] == 0:
                    tmp = dfs(sheeps+1, wolves, maxi)
                else:
                    tmp = dfs(sheeps, wolves+1, maxi)
                maxi = max(tmp, maxi)
                visit[c] = False
        return max(diff[0], maxi)
                
    visit[0] = True
    answer = dfs(1, 0, 0)
    
    return answer