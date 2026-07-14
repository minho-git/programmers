def solution(distance, rocks, n):
    answer = 0
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
   
    # 거리의 최솟값을 줄여나가보자.
    # 해당 거리일때 루프를 돌면서 바위를 몇개 제거해야하는지 체크
    # 바위를 n개보다 많이 제거해야한다 -> 실패 -> end = mid - 1
    # 바위를 n개보다 같거나 적게 제거했다 -> 성공 -> start = mid + 1
    # 우리가 구할게 거리의 최솟값의 최댓값이므로
    # 성공할때마다 최솟값의 최댓값을 구하자.
    start = 1
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        
        prev = 0
        
        for i in range(1, len(rocks)):
            tmp = rocks[i] - prev
            
            if tmp < mid: # 돌이 제거되야한다.
                count += 1
            else:
                prev = rocks[i]
        
        if count <= n:
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid -1
        
                
        
    
    
    return answer