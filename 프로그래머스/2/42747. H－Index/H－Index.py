def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    l = len(citations)
    print(citations)
    
    for i in range(l, -1, -1):
        tmp = 0
        for j in range(l):
            if citations[j] >= i:
                tmp += 1
        
        if tmp >= i:
            answer = i
            break
              
    return answer