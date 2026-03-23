import math

def solution(fees, records):
    for i in range(len(records)):
        tmp = records[i].split()
        time = tmp[0].split(":")
        hour = int(time[0])
        minute = int(time[1])
        total_minute =  hour * 60 + minute
        tmp[0] = total_minute
        
        records[i] = tmp
        # [분, 번호, 인/아웃]
        
    answer = []
    cars = {}
    default = 60 * 23 + 59
 
    for i in range(len(records)):
        info = records[i]
        
        if info[2] == "IN":
            cars[info[1]] = cars.get(info[1], 0) - info[0]
        else:
            cars[info[1]] = cars.get(info[1], 0) + info[0]

    

    for key, value in cars.items():
        if value <= 0:
            cars[key] += default
        
    
    for key, value in cars.items():
        cars[key] = value - fees[0]
        
        if cars[key] < 0:
            cars[key] = 0
            cars[key] = fees[1]
        else:
            cars[key] = fees[1] + math.ceil((cars[key] / fees[2])) * fees[3]
    
    
    array = sorted(cars)
    for key in array:
        answer.append(cars[key])
    
    
    return answer