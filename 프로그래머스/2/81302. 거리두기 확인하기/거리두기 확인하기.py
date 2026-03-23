def solution(places):
    answer = []
    for x in range(5):
        p = []
        for i in range(5):
            for j in range(5):
                if places[x][i][j] == "P":
                    p.append((i,j))
        
        if len(p) == 0:
            answer.append(1)
        elif len(p) == 1:
            answer.append(1)
        else:
            flag = 0
            for i in range(len(p)):
                if flag == 1:
                    break
                    
                for j in range(i+1, len(p)):
                    y1, x1 = p[i]
                    y2, x2 = p[j]
                        
                    # 바로 옆
                    if abs(y2-y1) + abs(x2-x1) == 1:
                        flag = 1
                        answer.append(0)
                        break
                            
                    elif abs(y2 - y1) + abs(x2 -x1) == 2:
                        # 가로: 한 칸 띄우고 옆
                        if y1 == y2:
                            if x2 > x1:
                                if places[x][y1][x1+1] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break
                            else:
                                if places[x][y1][x2+1] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break
                        # 세로: 한 칸 띄우고 옆 
                        elif x1 == x2:
                            if y2 > y1:
                                if places[x][y1+1][x1] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break
                            else:
                                if places[x][y2+1][x1] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break   
                        # 대각선
                        elif (y2 - y1) + (x2 - x1) == 0:
                            if y2 > y1:
                                if places[x][y2-1][x2] != "X" or places[x][y2][x2+1] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break
                            elif y2 < y1:
                                 if places[x][y1-1][x1] != "X" or places[x][y1][x1+1] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break   
                        else:
                            if y2 > y1:
                                if places[x][y2][x1] != "X" or places[x][y1][x2] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break
                            if y2 < y1:
                                if places[x][y1][x2] != "X" or places[x][y2][x1] != "X":
                                    flag = 1
                                    answer.append(0)
                                    break
                
            else:
                answer.append(1)
                    
                            
    
    return answer