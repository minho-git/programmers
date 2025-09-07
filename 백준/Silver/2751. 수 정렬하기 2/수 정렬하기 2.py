import sys

N = int(input())
nums_list = []

for i in range(N):
    nums_list.append(int(sys.stdin.readline()))

nums_list.sort()

for i in range(N):
    print(nums_list[i])
