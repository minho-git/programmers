def solution(distance, rocks, n):
    
    answer = distance
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    start = 1
    end = distance
    
    while start <= end:
        print(start, end)
        mid = (start + end) // 2
        count = 0
        prev = 0
        
        for i in range(1, len(rocks)):
            tmp = rocks[i] - prev
            
            if tmp < mid:
                count += 1                
            else:
                prev = rocks[i]
                
        
        if count > n:
            end = mid - 1   
        else: 
            start = mid + 1
            answer = mid
    
    
    return answer