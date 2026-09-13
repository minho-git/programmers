def solution(lottos, win_nums):
    answer = []
    pass_count = 0
    fail_count = 0
    _set = set()
    
    for win_num in win_nums:
        _set.add(win_num)
    
    for lotto in lottos:
        if lotto == 0:
            fail_count += 1
            
        elif lotto in _set:
            pass_count += 1
    
    _max = pass_count + fail_count
    
    if _max < 2:
        answer.append(6)
    else:
        answer.append(7-_max)
    
    if pass_count < 2:
        answer.append(6)
    else:
        answer.append(7-pass_count)
    

    return answer