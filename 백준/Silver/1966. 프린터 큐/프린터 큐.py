import heapq
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    prioritys = list(map(int, input().split()))
    max_heap = []
    queue = deque()

    for i in range(N):
        heapq.heappush(max_heap, -prioritys[i])

        queue.append((i, prioritys[i]))

    count = 1
    popped_heap = -heapq.heappop(max_heap)

    while queue:
        popped_queue = queue.popleft()
        index, priority = popped_queue[0], popped_queue[1]

        if priority == popped_heap:
            if index == M:
                print(count)
                break
            else:
                popped_heap = -heapq.heappop(max_heap)
                count += 1


        else:
            queue.append(popped_queue)

