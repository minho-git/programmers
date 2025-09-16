def confetti(confetties, y, x, length):
    global white_count, blue_count
    flag_0 = False
    flag_1 = False

    # 만약 크기가 1이라면 0이면 흰색++, 1이면 파란색++
    if length == 1:
        if confetties[y][x] == 0:
            white_count += 1
        else:
            blue_count += 1

        return

    # 모든 칸이 1인 또는 0인지 확인 -> return
    for i in range(length):
        for j in range(length):
            if confetties[y + i][x + j] == 0:
                flag_0 = True
            else:
                flag_1 = True

    if flag_0 and not flag_1:
        white_count += 1
    elif flag_1 and not flag_0:
        blue_count += 1
    else:
        # 모든 칸이 1 또는 0이 아니면, 4 조각 으로 짜르기
        confetti(confetties, y, x, length // 2)
        confetti(confetties, y +length//2, x, length // 2)
        confetti(confetties, y, x + length//2, length // 2)
        confetti(confetties, y + length//2, x + length//2, length // 2)


N = int(input())
board = []
white_count = 0
blue_count = 0

for i in range(N):
    board.append(list(map(int, input().split())))

start_size = len(board)
confetti(board, 0, 0, start_size)

print(white_count)
print(blue_count)
