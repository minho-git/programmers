def solution(s):
    arr = s.split(" ")
    res = ""
    
    print(arr)
    
    for i in range(len(arr)):
        res += arr[i].capitalize()
        
        if i != len(arr) -1:
            res += " "
              
            
    return res