def solution(X, Y):
    answer = ''
    
    x_dict = dict()
    y_dict = dict()
    nums = []
    
    # X에서 숫자 뽑기
    for num in X:
        x_dict[int(num)] = x_dict.get(int(num), 0) + 1
        
    # Y에서 숫잦 뽑기
    for num in Y:
        y_dict[int(num)] = y_dict.get(int(num), 0) + 1
    
    
    # 겹치는 숫자 찾기
    for num in X:
        if y_dict.get(int(num), 0) >= 1:
            nums.append(int(num))
            y_dict[int(num)] -= 1
            
    # 가장 큰수 
    nums.sort(reverse=True)
    
    
    if not nums:
        answer = "-1"
    
    else:
        
        for i in nums:
            answer += str(i)
            
        answer = str(answer)

    if answer[0] == "0":
        while "00" in answer:
            answer = answer.replace("00", "0")
        

            
    return answer