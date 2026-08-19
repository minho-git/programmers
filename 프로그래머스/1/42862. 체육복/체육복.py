def solution(n, lost, reserve):
    answer = 0
    
    students = [True] * (n+1)
    real = []
    
    for s in lost:
        students[s] = False
        
    for s in reserve:
        if s in lost:
            students[s] = True
        else:
            real.append(s)
            
    real.sort()
    
    for s in real:
        if not students[s-1]:
            students[s-1] = True
        elif s < n and not students[s+1]:
            students[s+1] = True
            
    for i in range(1, n+1):
        if students[i]:
            answer += 1
            
    return answer