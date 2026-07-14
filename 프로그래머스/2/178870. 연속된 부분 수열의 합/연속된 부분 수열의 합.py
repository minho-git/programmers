def solution(sequence, k):
    
    answer = []
    _min = len(sequence)
    start = 0
    end = 0
    tmp = sequence[start]
    
    while end < len(sequence) or start < len(sequence):
        
        if tmp == k:
            l = end - start
            if l < _min:
                _min = l
                answer = [start, end]
            
            end += 1
            
            if end == len(sequence):
                break
                
            tmp += sequence[end]
            
        
        elif tmp < k:
            end += 1
            
            if end == len(sequence):
                break
            tmp += sequence[end]
            
        elif tmp > k:
            tmp -= sequence[start]
            start += 1
            
    
    return answer