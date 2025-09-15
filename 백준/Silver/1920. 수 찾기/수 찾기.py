N = int(input())
nums = list(map(int, input().split()))

nums.sort()

M = int(input())
find_nums = list(map(int,input().split()))


for i in range(len(find_nums)):
    flag = False
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == find_nums[i]:
            print(1)
            flag = True
            break
        elif nums[mid] < find_nums[i]:
            start = mid + 1

        else:
            end = mid - 1

    if not flag:
        print(0)


