def solution(N, stages):
    total_count = [0] * (N+1)
    fail_count = [0] * (N+1)
    
    for stage in stages:
        if stage == N+1:
            for i in range(1, N+1):
                total_count[i] += 1
        else:
            for i in range(1, stage+1):
                total_count[i] += 1
        
            fail_count[stage] += 1
    
    rank = []
    for i in range(1, N+1):
        if total_count[i] == 0:
            rank.append((i, 0))
        else:
            rank.append((i, fail_count[i] / total_count[i]))
    
    rank.sort(key = lambda x : x[1], reverse=True)
    
    answer = [a for a, b in rank]
    return answer