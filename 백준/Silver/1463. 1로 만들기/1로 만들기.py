from collections import deque

n = int(input())

visited = [False for i in range(1000000 + 1)]
queue = deque()
queue.append((1, 0))

while True:

    value, count = queue.popleft()

    if value == n:
        print(count)
        break

    tmp = 3 * value
    if  tmp < len(visited) and not visited[tmp]:
        queue.append((tmp, (count + 1)))
        visited[tmp] = True

    tmp = 2 * value
    if tmp < len(visited) and not visited[tmp]:
        queue.append((tmp, (count + 1)))
        visited[tmp] = True

    tmp = 1 + value
    if tmp < len(visited)  and not visited[tmp]:
        queue.append((tmp, (count + 1)))
        visited[tmp] = True

