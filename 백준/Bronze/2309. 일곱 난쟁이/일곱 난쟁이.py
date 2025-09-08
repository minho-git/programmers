# 1. 재귀

# def 난쟁이찾기(count,  result, total):
#     global heights, flag
#
#     if len(result) == 7 and total == 100:
#         result.sort()
#         for i in range(7):
#             print(result[i])
#         flag = False
#         return
#
#     elif len(result) > 7 or total > 100 or count == 9:
#         return
#
#     elif flag:
#         result.append(heights[count])
#         난쟁이찾기(count + 1, result, total + heights[count])
#         result.pop()
#         난쟁이찾기(count + 1, result, total)
#
# # 배열에 다 집어넣는다.
# heights = []
# flag = True
#
# for i in range(9):
#     heights.append(int(input()))
#
# # 완전 탐색으로 난쟁이 찾기 시작
# result = []
# 난쟁이찾기(0, result, 0)

# 2. 메서드 이용

import itertools

# 배열에 다 집어넣는다.
# heights = []
#
# for i in range(9):
#     heights.append(int(input()))
#
# # itertools.combinations(이터레이터, 갯수): 조합을 구해준다.
# for comb in itertools.combinations(heights, 7):
#     if sum(comb) == 100:
#         comb = sorted(comb)
#         for i in range(7):
#             print(comb[i])


# 3. for문 이용
# 9명중 7명의 합을 하나 하나 더하는 경우 7중 for문이 필요하다.
# 반대로 9명의 합에서 두 개를 뺏을 때 100인 경우를 구해보자

heights = []

for i in range(9):
    heights.append(int(input()))

total = sum(heights)
heights.sort()

for i in range(len(heights)-1):
    for j in range(i+1, len(heights)):
        if total - heights[i] - heights[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(heights[k])
            exit()
        else:
            continue

            
            









