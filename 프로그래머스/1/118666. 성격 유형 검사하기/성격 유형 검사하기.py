def solution(survey, choices):
    answer = ''
    result = []
    지표들 = {}
    
    지표들[1] = {"R" : 0, "T" : 0}
    지표들[2] = {"C" : 0, "F" : 0}
    지표들[3] = {"J" : 0, "M" : 0}
    지표들[4] = {"A" : 0, "N" : 0}
    
    for i in range(len(survey)):
        _type = 0
        
        s = survey[i]
        c = choices[i]
        
        # 지표 결정
        
        if "R" in s:
            _type = 1
            
        elif "C" in s:
            _type = 2
            
        elif "J" in s:
            _type = 3
            
        elif "A" in s:
            _type = 4
        
        
        # 점수 누구한테 줄지 결정하고 점수 부여
        if c == 4:
            continue
                 
        if c < 4:
            지표들[_type][s[0]] += (8 - c) % 4
        else:
            지표들[_type][s[1]] +=  c % 4

    
    for i in range(1, 5):
         result.append(list(sorted(지표들[i].items(), key = lambda x : x[1], reverse=True)))
        
    print(result)
    for t in result:
        answer+= t[0][0]
    
    return answer