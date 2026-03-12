def solution(new_id):
    
    # 1.
    res1 = new_id.lower()
    
    # 2.
    res2 = ""
    for i in range(len(res1)):
        tmp = res1[i]
        if tmp.isalpha() or tmp.isdigit() or tmp in ("_", ".", "-"):
            res2 += tmp

    # 3.
    res3 = res2[0]
    for i in range(1, len(res2)):
        if res3[-1] != "." or res2[i] != ".":
            res3 += res2[i]
    
    # 4.
    if res3[0] == ".":
        res3 = res3[1:]
    
    res4 = ""
    if len(res3) > 0 and res3[-1] == ".":
        res4 = res3[:-1]
    else:
        res4 = res3
    
    # 5.
    res5 = ""
    if res4 == "":
        res5 = "a"
    else:
        res5 = res4  
    
    # 6.
    res6 = ""
    if len(res5) > 15:
        res6 = res5[:15]
    else:
        res6 = res5
    
    if res6[-1] == ".":
        res6 = res6[:-1]
    
    # 7.
    res7 = ""
    if len(res6) < 3:
        res7 = res6
        
        while len(res7) != 3:
            res7 += res7[-1]
    else:
        res7 = res6

    return res7