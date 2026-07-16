def solution(people, limit):
    people.sort()
    answer = 0

    # 제일 작은거랑 더했을때 리미트를 넘는거면 무조건 혼자 타야한다!
    start = 0
    end = len(people) - 1
    
    while start <= end:
        tmp = people[start] + people[end]
        answer += 1
        
        if tmp > limit:
            end -= 1
        else:
            start += 1
            end -= 1
    
    
    return answer