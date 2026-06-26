from collections import Counter

def solution(participant, completion):
    tmp = {}
    answer = ""

    for a in participant:
        tmp[a] = tmp.get(a, 0) + 1
    
    
    for b in completion:
        if tmp.get(b) > 1:
            tmp[b] = tmp[b] - 1
        else:
            del tmp[b]
    
    for key in tmp.keys():
        answer = key
        
    return answer