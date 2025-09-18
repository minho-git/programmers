import heapq
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    중요도 = list(map(int, input().split()))
    max_heap = []
    큐 = deque()

    for i in range(N):
        # 힙에 저장하자. 
        heapq.heappush(max_heap, -중요도[i])

        # 큐에 인덱스랑 같이 저장하자.
        큐.append((i, 중요도[i]))

    count = 1
    힙에서뺀것 = -heapq.heappop(max_heap)


    # 계속 반복하자.
    while 큐:
        큐에서뺀것 = 큐.popleft()
        index, 중요도값 = 큐에서뺀것[0], 큐에서뺀것[1]

        if 중요도값 == 힙에서뺀것:
            if index == M:
                print(count)
                break
            else:
                힙에서뺀것 = -heapq.heappop(max_heap)
                count += 1


        else:
            큐.append(큐에서뺀것)

