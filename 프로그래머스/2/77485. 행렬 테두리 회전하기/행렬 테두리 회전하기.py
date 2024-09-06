def debug_2d_graph(graph):
    for g in graph:
        print(g)
        
def rotate_graph(graph, x1, y1, x2, y2):
    tmp = graph[y1][x1]
    
    # LEFT
    for y in range(y1, y2-1):
        graph[y][x1] = graph[y+1][x1]
        
    # BOTTOM
    for x in range(x1, x2-1):
        graph[y2][x] = graph[y2][x+1]

    # RIGHT
    for y in range(y2, y1+1, -1):
        graph[y][x2] = graph[y-1][x2]
                
    # TOP
    for x in range(x2, x1+1, -1):
        graph[y1][x] = graph[y1][x-1]
        
    graph[y1][x1+1] = tmp
    
    return graph
        
def solution(rows, columns, queries):
    answer = []
    
    graph = [[0] * columns for _ in range(rows)]
    
    i = 1
    for row in range(rows):
        for col in range(columns):
            graph[row][col] = i
            i += 1
    
    debug_2d_graph(graph)
    graph = rotate_graph(graph, 1, 1, 4, 3)
    debug_2d_graph(graph)
    
    return answer