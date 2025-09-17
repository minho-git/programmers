import heapq
import sys

N = int(input())

min_heap = []
max_heap = []

for i in range(N):
    num = int(sys.stdin.readline())

    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if len(min_heap) + 1 < len(max_heap) :
        tmp = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, tmp)
    elif len(min_heap) > len(max_heap):
        tmp = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -tmp)
    print(-1 * max_heap[0])


