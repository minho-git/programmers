def solution(distance, rocks, n):
    answer = 0
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    
    # 최댓값은 distance, 최솟값은 1
    start = 1
    end = distance
    
    while start <= end:
        _min = distance
        mid = (start + end) // 2
        
        removed = 0
        prev = 0
        # 돌의 간격이 mid 값보다 작으면 돌을 제거해야한다.
        # 제거한 돌의 갯수가 n보다 작으면 탈락
        # 제거한 돌의 갯수가 n보다 크거나 같으면 성공
        for i in range(1, len(rocks)):
            tmp = rocks[i] - prev
            _min = min(_min, tmp)
            if tmp < mid:
                removed += 1
            else:
                prev = rocks[i]
                
        if removed <= n:
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1
            
        
    return answer