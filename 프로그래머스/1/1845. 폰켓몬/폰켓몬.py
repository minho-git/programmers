def solution(nums):
    뽑을수 = len(nums) // 2
    도감 = set()
    answer = 0
    
    for num in nums:
        도감.add(num)
        
    포켓몬수 = len(도감)
    if 포켓몬수 >= 뽑을수:
        answer = 뽑을수
    else:
        answer = 포켓몬수
        
    
    return answer