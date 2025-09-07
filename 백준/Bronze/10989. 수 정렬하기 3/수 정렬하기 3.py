import sys

N = int(sys.stdin.readline())
nums_count_list = [0] * 10001


for i in range(N):
    num = int(sys.stdin.readline())
    nums_count_list[num] = nums_count_list[num] + 1

for i in range(10001):
    for j in range(nums_count_list[i]):
        print(i)
