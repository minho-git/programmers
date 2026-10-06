def solution(new_id):
    
    # 1단계
    result_1 = new_id.lower()
    
    # 2단계
    result_2 = []
    for c in result_1:
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            result_2.append(c)
            
    result_2 = "".join(result_2)
    
    # 3단계
    tmp = result_2[0]
    result_3 = [tmp]
    for i in range(1, len(result_2)):
        if tmp == "." and result_2[i] == ".":
            pass
        else:
            result_3.append(result_2[i])
            tmp = result_2[i]

            
    result_3 = "".join(result_3)
    
    # 4단계
    result_4 = result_3
    if result_4 and result_4[0] == '.':
        result_4 = result_4[1:]
    
    if result_4 and result_4[-1] == '.':
        result_4 = result_4[:-1]
        
    
    # 5단계
    result_5 = ""
    if not result_4:
        result_5 = "a"
    else:
        result_5 = result_4
        
    # 6단계
    result_6 = ""
    if len(result_5) >= 16:
        result_6 = result_5[:15]
        
        if result_6[-1] == ".":
            result_6 = result_6[:-1]
    else:
        result_6 = result_5
        
    
    # 7단계
    result_7 = result_6
    if len(result_7) <= 2:
        
        while len(result_7) != 3:
            result_7 += result_7[-1]
            
    return result_7
  