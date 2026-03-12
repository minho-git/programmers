import math

def solution(progresses, speeds):
    
    days = []
    answer = []

    for i in range(len(progresses)):
        remains = 100 - progresses[i]
        days.append(math.ceil(remains / speeds[i]))
        
    now = days[0]
    count = 1
    for i in range(1, len(days)):
        if days[i] <= now:
            count += 1
        else:
            answer.append(count)
            now = days[i]
            count = 1
            
    answer.append(count)
    return answer