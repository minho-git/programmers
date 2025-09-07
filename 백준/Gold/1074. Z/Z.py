# def z(size, y, x):
#     global r, c
#     global count
#     global board
#
#     if size == 2:
#         board[y-1][x-1] = count
#         count += 1
#
#         board[y-1][x] = count
#         count += 1
#
#         board[y][x-1] = count
#         count += 1
#
#         board[y][x] = count
#         count += 1
#
#         return
#
#     다음크기= size // 2
#
#     z(다음크기,  y - (다음크기 // 2), x - (다음크기 // 2))
#     z(다음크기,  y - (다음크기 // 2), x + (다음크기 // 2))
#     z(다음크기,  y + (다음크기 // 2), x - (다음크기 // 2))
#     z(다음크기,  y + (다음크기 // 2), x + (다음크기 // 2))
#
#
# N, r, c = map(int, input().split())
#
# size = 2 ** N
# count = 0
#
# # board = [[0] * (2 * N)] * (2 * N) # 같은 리스트를 여러 개 생성
# board = [[0] * size for _ in range(size)] # 새로운 리스트를 여러 개 생성
#
# z(size , size//2, size//2)
#

def 제트함수(n, start_number, y, x):

    if n == 1:
        if y == 0 and x == 0:
            print(start_number)
        elif y == 0 and x == 1:
            print(start_number + 1)
        elif y == 1 and x == 0:
            print(start_number + 2)
        else:
            print(start_number + 3)

        return

    size = 2 ** n
    # N = 1일때 2의 0승차이 -> 2의 (1 * 2) / 2의 2승 -> 2의 0승
    # N = 2일때 2의 2승차이 -> 2의 (2승 * 2) / 2의 2승 -> 2의 2승
    # N = 3일때 2의 4승차이 -> 2의 (3승 * 2) / 2의 2승 -> 2의 4승

    gap = 2 ** (n * 2 - 2) # gap = 16
    if y < size // 2 and x < size // 2:
        제트함수(n - 1, start_number, y, x)
    elif y < size // 2 <= x:
        제트함수(n - 1, start_number + gap, y, x - (size // 2))
    elif y >= size // 2 > x:
        제트함수(n - 1, start_number + (2 * gap), y - (size // 2), x)
    else:
        제트함수(n - 1, start_number + (3 * gap), y - (size // 2), x - (size // 2))

N, y, x = map(int, input().split())
제트함수(N, 0, y, x)






