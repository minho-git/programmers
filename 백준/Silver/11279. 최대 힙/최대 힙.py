import heapq
import sys

heap = []

n = int(sys.stdin.readline())

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            pop_item = -1 * heapq.heappop(heap)
            print(pop_item)

    else:
        heapq.heappush(heap, -1 * x)