##############
##  Solution with DFS
##############
def solution(n, computers):
            
    def dfs(com):  # dfs 한번 돌고나면 방문했던 네트워크들은 visit = True로 바꿔놓는다
        visited[com] = True
        for i in range(n):
            if i != com and computers[com][i] == 1:  # 자신을 제외하고 연결된 컴퓨터
                if visited[i] == False:
                    dfs(i)
    
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:  # 아직 방문 안한 노드가 있으면 dfs 돌린다.
            dfs(com)
            answer += 1
        


    return answer

##############
##  Solution with BFS
##############

from collections import deque

def solution(n, computers):
    
    visit = [False] * n
    
    def bfs(x):
        visit[x] = True
        Q = deque()
        Q.append(x)
        
        while Q:
            com = Q.popleft()  # 다음 방문할 노드의 index
            for i in range(n):
                if i == com:
                    continue
                if visit[i] == False and computers[com][i] == 1:
                    visit[i] = True
                    Q.append(i)
    answer = 0
    
    for i in range(n):
        if visit[i] == False:
            answer += 1
            bfs(i)
    
    return answer