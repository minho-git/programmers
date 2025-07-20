def solution(numbers, target):
    answer = get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target)
    return answer

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    count = 0
    result = 0
    index = 0

    def dfs(index, result):
        if index == len(array):
            if result == target:
                nonlocal count
                count += 1
            return
        else:
            dfs(index + 1, result + array[index])
            dfs(index + 1, result - array[index])

    dfs(index, result)

    return count
