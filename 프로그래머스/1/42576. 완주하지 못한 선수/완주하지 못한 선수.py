def solution(participant, completion):
    a = {}
    res = []
    for x in completion:
        a[x] = a.get(x, 0) + 1
    
    for x in participant:
        if x not in a:
            res.append(x)
        else:
            if a[x] == 0:
                res.append(x)
            else:
                a[x] -= 1
    
    return res[0]