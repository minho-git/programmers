n = int(input())

dp = [0 for i in range(n+1)]

lst = list(map(int, input().split()))
lst.insert(0, 0)

dp[1] = 1

for i in range(2, n+1):
    for j in range(i-1, 0, -1):

        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j])

    dp[i] += 1

# 자기 보다 작은 값의 최대 인덱스 를 구해라
# +1 한걸 넣는다.

print(max(dp))
