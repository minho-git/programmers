from collections import Counter

def solution(k, tangerine):
    res = 1
    answer = 0
    t = dict()
    for i in range(len(tangerine)):
        t[tangerine[i]] = t.get(tangerine[i], 0) + 1
    
    l = []
    for key, value in t.items():
        l.append((key, value))
    
    l.sort(key=lambda x:x[1], reverse=True)
    
    for source, count in l:
        if k - count <= 0:
            answer = res
            break
        else:
            k -= count
            res += 1
            

    return answer