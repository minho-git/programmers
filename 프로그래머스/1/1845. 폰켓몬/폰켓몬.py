def solution(nums):

    N = len(nums)
    
    arr = set(nums)
    M = len(arr)
    
    
    if N//2 >= M:
        return M
    else:
        return N//2
