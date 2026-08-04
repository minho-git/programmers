def solution(rows, columns, queries):
    answer = []
    
    graph =[[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = columns * i + (j+1)
    
    for query in queries:
        _min = int(1e9)
        x1, y1, x2, y2 = tuple(query)
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        
        point_1 = graph[x1][y1]
        point_2 = graph[x1][y2]
        point_3 = graph[x2][y2]
        point_4 = graph[x2][y1]
        
        _min = min(_min, point_1, point_2, point_3, point_4)
            
        
        for x in range(x1, x2):
            graph[x][y1] = graph[x+1][y1]
            graph[x2-(x-x1)][y2] = graph[x2-(x-x1)-1][y2]
            
            _min = min(graph[x][y1], graph[x2-(x-x1)][y2], _min)
        
        for y in range(y1, y2):
            graph[x1][y2-(y-y1)] = graph[x1][y2-(y-y1)-1]
            graph[x2][y] = graph[x2][y+1]
        
            _min = min(graph[x1][y2-(y-y1)], graph[x2][y], _min)
            
        graph[x1][y1+1] = point_1
        graph[x1+1][y2] = point_2
        graph[x2][y2-1] = point_3
        graph[x2-1][y1] = point_4
        
        
        answer.append(_min)
    
    
    return answer