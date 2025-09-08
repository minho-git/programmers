def 난쟁이찾기(count,  result, total):
    global heights, flag

    if len(result) == 7 and total == 100:
        result.sort()
        for i in range(7):
            print(result[i])
        flag = False
        return
        
    elif len(result) > 7 or total > 100 or count == 9:
        return
        
    elif flag:
        result.append(heights[count])
        난쟁이찾기(count + 1, result, total + heights[count])
        result.pop()
        난쟁이찾기(count + 1, result, total)

# 배열에 다 집어넣는다.
heights = []
flag = True

for i in range(9):
    heights.append(int(input()))

# 완전 탐색으로 난쟁이 찾기 시작
result = []
난쟁이찾기(0, result, 0)








