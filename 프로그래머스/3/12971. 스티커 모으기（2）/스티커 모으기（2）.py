def solution(sticker):
    answer = 0

    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)

    # 첫 번째 스티커를 땟을 때
    for i in range(len(sticker)-1):
        if i == 0:
            dp1[0] = sticker[0]
        elif i == 1:
            dp1[1] = max(dp1[0], sticker[1])
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # 첫 번째 스티커를 안 땟을 때
    for i in range(1, len(sticker)):
        if i == 1:
            dp2[1] = sticker[1]
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    if len(sticker) == 1:
        answer = sticker[0]
    else:
        answer = max(max(dp1), max(dp2))    
    return answer