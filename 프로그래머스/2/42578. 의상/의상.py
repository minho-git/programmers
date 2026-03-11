from collections import Counter

def solution(clothes):
#     _dict = {}
    
#     for cloth in clothes:
#         if _dict.get(cloth[1], 0) == 0:
#             _dict[cloth[1]] = [cloth[0]]
#         else:
#             _dict[cloth[1]].append(cloth[0])
    
#     res = []
#     for x in _dict.values():
#         res.append(len(x)+1)
    
#     print(_dict)
#     print(res)
#     total = 1
#     for x in res:
#         total *= x
    
#     return total - 1

    type = []
    for cloth in clothes:
        type.append(cloth[1])
    
    c = list(Counter(type).values())
    res = 1
    for x in c:
        res *= x + 1
    
    return res - 1