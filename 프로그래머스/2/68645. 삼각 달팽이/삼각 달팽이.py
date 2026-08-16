def solution(n):
    answer = []
    
    # 카운트만큼 돌아야 한다.
    count = (n * (n + 1)) // 2 - 1
    
    # 미리 그래프 세팅
    graph = [[0] * i for i in range(1, n+1)]
    graph[0][0] = 1
    tmp = n-1
    num = 1
    row = 0
    column = 0
    
    for i in range(tmp):
        row += 1        
        num += 1
        graph[row][column] = num
        count -= 1
    
    for i in range(tmp):
        column += 1    
        num += 1
        graph[row][column] = num
        count -= 1
    
    tmp -= 1

    while count > 0:
        
        # 행 -1, 열 -1 반복
        for i in range(tmp):
            if count <= 0:
                break
                
            row -= 1
            column -= 1
            num += 1
                
            graph[row][column] = num
            count -= 1
            
        tmp -= 1
        
        # 행 + 1 반복
        for i in range(tmp):
            if count <= 0:
                break
                
            row += 1
            num += 1
            graph[row][column] = num
            count -= 1
            
        tmp -= 1
        
        # 열 + 1 반복
        for i in range(tmp):
            if count <= 0:
                break
                
            column += 1
            num += 1
            graph[row][column] = num
            count -= 1
            
        tmp -= 1
        
    # 정답에 넣기
    for i in range(0, n):
        for j in range(0, i+1):
            answer.append(graph[i][j])
    
    return answer