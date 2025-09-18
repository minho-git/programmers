N = int(input())
상근이카드들 = list(map(int, input().split()))
상근이카드들.sort()
result = []

M = int(input())
정수들 = list(map(int,input().split()))



for i in range(M):
    확인할카드 = 정수들[i]
    flag = False
    start = 0
    end = len(상근이카드들) - 1

    while(start <= end):
        mid = (start + end) // 2

        if 상근이카드들[mid] == 확인할카드:
            result.append(1)
            flag = True
            
            break
        
        if 상근이카드들[mid] > 확인할카드:
            end = mid - 1
        
        elif 상근이카드들[mid] < 확인할카드:
            start = mid + 1
        
    if not flag:
            result.append(0)

for i in result:
     print(i, end = " ")