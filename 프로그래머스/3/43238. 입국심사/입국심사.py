def solution(n, times):
    answer = 0
    
    # 시간 최소를 알고, 최대를 아니깐 -> 최솟값 구하기는 이분 탐색
    # 최소는 min(times), 최대는 max(times) * n
    
    start = min(times)
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        
        # 여기서 성립하는지 체크
        # 어떻게 성립하는지 확인할까?
        # 각 시간을 돌면서 시간안에 몇명 처리가 가능한지 다 더하자.
        # 그 결과가 n보다 크거나 같으면 성공, 아님 실패
        # 성공하면 end = mid - 1, 실패하면 start = mid + 1
        
        _sum = 0
        
        for time in times:
            _sum += mid // time
        
        if _sum >= n:
            end = mid - 1
            answer = mid
            
        else:
            start = mid + 1
        
        
        
        
    
    return answer