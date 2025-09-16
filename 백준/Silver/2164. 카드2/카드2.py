from collections import deque

# 1. N 입력받기
N = int(input())
queue = deque()

# 2. 큐에 1부터 N까지 집어넣기
for i in range(1, N+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    poped = queue.popleft()
    queue.append(poped)

print(queue[0])

# 3. 카드가 한장 남을 때까지
# 제일 위에있는 카드를 버린다
# 제일 위에있는 카드를 제일 밑으로 옮긴다.

# 4. 큐에 마지막으로 있는 것 출력