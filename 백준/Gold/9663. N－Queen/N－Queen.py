def queen(y, column, cross_line_right, cross_line_left):
    global answer, N

    if y > N:
        answer += 1
        return



    for j in range(1, N+1):
        if not column[j] or not cross_line_right[y - j + N] or not cross_line_left[y+j]:
            continue

        # 세로 안되게하기
        column[j] = False
        cross_line_right[y - j + N] = False
        cross_line_left[y + j] = False

        queen(y+1, column, cross_line_right, cross_line_left)

        column[j] = True
        cross_line_right[y - j + N] = True
        cross_line_left[y + j] = True

N = int(input())

answer = 0

# 첫 번째 행 첫번째 열부터 마지막 열까지 해보기
# set은 set()으로 만들어야 함
column = [True] * (N+1)
cross_line_right = [True] * ((2 * N) + 1)
cross_line_left = [True] * ((2 * N) + 1)

queen(1, column, cross_line_right, cross_line_left)

print(answer)




