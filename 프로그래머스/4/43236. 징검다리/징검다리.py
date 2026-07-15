def solution(distance, rocks, n):
    # 이 문제는 일단 이분 탐색임을 인지한다.
    # 거리의 최솟값의 최댓값을 구해라. 및 범위가 1,000,000,000
    # 이분탐색!
    
    # 최소, 최대를 구해야한다.
    # 최소는 1, 최대는 distance
    
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    start = 1
    end = distance
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        _min = distance
        
        # 여기서 돌 몇 개 제거가능한지 체크
        # prev를 꼭 기억해두자. 왜냐하면 돌을 제거했으면 과거의 돌과 거리를 비교해야하기때문에
        prev = 0
        count = 0
        
        for i in range(1, len(rocks)):
            tmp = rocks[i] - prev
            
            if tmp < mid:
                count += 1
            else:
                prev = rocks[i]
                _min = min(_min, tmp)
        
        if count > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = max(answer, _min)
            
            
                
            
    
    
    return answer