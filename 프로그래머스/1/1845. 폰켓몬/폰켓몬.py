def solution(nums):

    l = len(nums) // 2
    c = set() # 이거 왜 그냥 {}로 하면 안돼?
    result = 0
    
    for num in nums:
        if result >= l:
            break
        
        if num not in c:
            result += 1
            c.add(num)
    
    
    return result
    
