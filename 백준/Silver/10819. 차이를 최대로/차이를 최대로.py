def dif_to_max(result, flags, dif_sum, count):
    global dif_sum_max
    for i in range(N):
        if count == N:
            if dif_sum_max < dif_sum:
                dif_sum_max = dif_sum
                return

        if flags[i]:
            result.append(nums[i])
            dif_sum += abs(result[-1] - result[-2])
            flags[i] = False
            dif_to_max(result, flags, dif_sum, count + 1)
            dif_sum -= abs(result[-1] - result[-2])
            flags[i] = True
            result.pop()



N = int(input())
nums = list(map(int, input().split()))
dif_sum_max = 0

for i in range(N):
    result_array = [nums[i]]
    flags_array = [True] * N
    flags_array[i] = False

    dif_to_max(result_array, flags_array, 0, 1)

print(dif_sum_max)
