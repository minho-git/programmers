import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
answer = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in range(len(trees)):
        diff = trees[i] - mid
        if diff > 0:
            total += diff

    if total >= M:
        answer = mid
        start = mid + 1

    else:
        end = mid - 1

print(answer)