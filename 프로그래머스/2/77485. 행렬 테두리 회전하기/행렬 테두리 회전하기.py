def solution(rows, columns, queries):
    answer = []
    
    # 채워넣기
    graph = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = (i * columns) + j + 1
    
    
    # 쿼리 반복
    for query in queries:
        _min = int(1e9)

        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1

        # 포인트값 기억하기
        point_1 = graph[x1][y1]
        point_2 = graph[x2][y2]
        
        # 세로 회전하기
        for x in range(x1, x2):
            graph[x][y1] = graph[x+1][y1]
            _min = min(_min, graph[x][y1])
        
        for x in range(x2, x1, -1):
            graph[x][y2] = graph[x-1][y2]
            _min = min(_min, graph[x][y2])
        
        # 가로 회전하기
        for y in range(y2, y1+1, -1):
            graph[x1][y] = graph[x1][y-1]
            _min = min(_min, graph[x1][y])
        
        for y in range(y1, y2-1):
            graph[x2][y] = graph[x2][y+1]
            _min = min(_min, graph[x2][y])

        # 포인트값으로 덮어쓰기
        graph[x1][y1+1] = point_1
        graph[x2][y2-1] = point_2
        
        _min = min(_min, graph[x1][y1+1], graph[x2][y2-1])
        answer.append(_min)
        
    
    return answer