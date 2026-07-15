def solution(n, times):
    answer = 0
   
    # 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
    start = min(times)
    end = max(times) * n
    
    while start <= end:
        
        mid = (start + end) // 2
        _sum = 0
        
        # 왜 이렇게 하는가?
        # 모두 한명씩 계속 처리한다하면 최대이지 않은가?
        # 그럼 최대가 만족할때 최솟값을 구하면 되는건가
        for time in times:
            _sum += (mid // time)
        
        if _sum >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
            
        

    return answer