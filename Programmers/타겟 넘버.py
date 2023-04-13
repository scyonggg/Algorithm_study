"""
완전 탐색 ㄱ
"""
answer = 0
def solution(numbers, target):
    
    def dfs(acc, idx):
        global answer
        if idx == len(numbers):
            if acc == target:
                answer += 1
            return
        else:
            dfs(acc + numbers[idx], idx + 1)
            dfs(acc - numbers[idx], idx + 1)
        return
            
    dfs(0, 0)
    
    return answer