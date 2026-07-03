from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

def solution(numbers):
    
    numbers_str = [str(number) for number in numbers]
    numbers_str.sort(key=cmp_to_key(compare))
    
    answer = ""
    for number_str in numbers_str:
        answer += number_str
        
    if answer[0] == "0":
        answer = "0"
    return answer