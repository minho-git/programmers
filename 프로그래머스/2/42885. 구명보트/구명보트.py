def solution(people, limit):
    answer = 0
    
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    while start <= end:
        
        tmp = people[start] + people[end]
        if tmp <= limit:
            answer += 1
            start += 1
            end -= 1
        else:
            answer += 1
            end -= 1
    
    return answer