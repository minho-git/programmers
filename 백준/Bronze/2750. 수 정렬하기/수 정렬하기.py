N = int(input())
nums = set()

for i in range(N):
    nums.add(int(input()))

nums = list(nums)
nums.sort()

for i in range(N):
    print(nums[i])

