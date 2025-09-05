N = int(input())
# array = [0] * 1001
#
# for i in range(1, 100):
#     array[i] = 1
#
#
# # 1부터 99까지 한수
# # 100부터 999까지 한수구해야함
#
# for i in range(100, 1000):
#     num = i #123
#     last = num % 10 #3
#     num = num // 10 # num = 12
#     mid = num % 10 # 2
#     num = num // 10 # num =1
#     first = num % 10 #1
#
#     if (last - mid) == (mid - first):
#         array[i] = 1
#
#
# count = 0
# for i in range(1, N+1):
#     if array[i] == 1:
#         count += 1
#
#
#
# print(count)

# array 안쓰고 풀어보기

count = 0
for i in range(1, N+1):
    if i < 100:
        count = i

    else:
        s = str(i)
        if int(s[2]) - int(s[1]) == int(s[1]) - int(s[0]):
            count += 1

print(count)
