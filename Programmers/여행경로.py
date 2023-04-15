from collections import deque
def solution(tickets):
    answer = []

    graph = {i[0]:[] for i in tickets}
    for i in tickets:
        graph[i[0]].append(i[1])
    for i in graph.keys():
        graph[i].sort(reverse=True)  # 스택 활용 위해


    def dfs():
        stack = ['ICN']
        while stack:
            start = stack[-1]
            print(f'start : {start}, stack : {stack}, answer : {answer}')
            if not start in graph.keys() or len(graph[start]) == 0:
                answer.append(stack.pop())
            else:
                stack.append(graph[start].pop())
    dfs()
    answer.reverse()

    return answer