from itertools import combinations

def solution(numbers):
    return sorted({a + b for a, b in combinations(numbers, 2)})
    