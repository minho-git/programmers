# 처음에 안익은 것들(0)의 갯수를 저장하자.
# 상자를 돌면서 1인 것을 만나면 상하좌우로 0인 것들을 1로 만들기
# 안익은 것들의 갯수가 0이면 종료하고 날짜(Level) 출력
# 갯수가 위에꺼랑 똑같다? 더 이상 익지않은것으로 -1 출력

from collections import deque
import sys

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

M, N = map(int, input().split()) # 가로, 세로
graph = []
q = deque()
day = 0

# 그래프 채우기
for i in range(N):
    graph.append(list(map(int, input().split())))

# 0의 갯수를 세자.
count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count += 1
        elif graph[i][j] == 1:
            q.append((i, j))

if count == 0:
    print(0)
    sys.exit() # sys 붙여야함!!

while q:
    # 갯수 변함이 없는지 체크
    day += 1

    # 큐의 길이만큼 반복해서 하나씩 빼서 상하좌우 채워넣기
    for i in range(len(q)):
        y, x = q.popleft()
        for j in range(4):
            yy = y + dy[j]
            xx = x + dx[j]

            if 0 <= yy < N and 0 <= xx < M and graph[yy][xx] == 0:
                count -= 1
                graph[yy][xx] = -1
                q.append((yy, xx))

    if count == 0:
        print(day)
        break

if count > 0:
    print(-1)
