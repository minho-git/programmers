import itertools

def check(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True        
    

def solution(numbers):
    answer = 0
    _set = set()
    
    for i in range(1, len(numbers)+1):
        for t in itertools.permutations(numbers, i):
            _set.add(int("".join(t)))
    
    for num in _set:
        if check(num):
            answer += 1
    
    return answer