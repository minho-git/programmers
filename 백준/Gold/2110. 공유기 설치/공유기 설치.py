import sys

N, C = map(int, input().split())

# 1. 집을 입력받고, 크기 순으로 정렬한다.
houses = []
for i in range(N):
    houses.append(int(sys.stdin.readline()))

houses.sort()

start = 1
end = houses[-1] - houses[0]
answer = 0

# 2. 가장 작은 값부터 가장 큰 값까지 mid 값으로 더해본다.
while start <= end:
    mid = (start + end) // 2
    last = houses[0]

    # 첫 번째 집에 공유기 설치 했으니깐 count는 1부터 시작
    count = 1

    for i in range(1, N):
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]

    if count >= C:
        start = mid + 1
        answer = max(answer, mid)
    elif count < C:
        end = mid - 1


print(answer)






