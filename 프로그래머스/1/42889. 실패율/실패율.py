def solution(N, stages):
    remaining = len(stages)
    fail_count = [0] * (N+2)
    
    rate = {}
    
    for stage in stages:
        fail_count[stage] += 1
    
    for i in range(1, N+1):
        if remaining == 0:
            rate[i] = 0
        else:   
            rate[i] = fail_count[i] / remaining
            remaining -= fail_count[i]
        
        
    return sorted(rate, key = lambda i : -rate[i])