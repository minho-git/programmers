from collections import deque       
    
def solution(board):
    answer = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    visited_garo = [[float("inf")] * (len(board)) for _ in range(len(board))]
    visited_sero = [[float("inf")] * (len(board)) for _ in range(len(board))]

    
    q = deque()
    visited_garo[0][0] = 0
    visited_sero[0][0] = 0
    q.append((0, 0, 0, "start")) # y, x, total
    
    while q:
        y, x, total, _type = q.popleft()
        
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            
            if 0 <= yy < len(board) and 0 <= xx < len(board) and board[yy][xx] == 0:
                if i in [0, 1]:
                    if _type in ["start", "세로"]:
                        new_total = total + 100
                        if new_total < visited_sero[yy][xx]:
                            q.append((yy, xx, new_total, "세로"))
                            visited_sero[yy][xx] = new_total
                    else:
                        new_total = total + 600
                        if new_total < visited_sero[yy][xx]:
                            q.append((yy, xx, new_total, "세로"))
                            visited_sero[yy][xx] = new_total

                    
                    
                elif i in [2, 3]:
                    if _type in ["start", "가로"]:
                        new_total = total + 100
                        if new_total < visited_garo[yy][xx]:
                            q.append((yy, xx, new_total, "가로"))
                            visited_garo[yy][xx] = new_total

                    else:
                        new_total = total + 600
                        if new_total < visited_garo[yy][xx]:
                            q.append((yy, xx, new_total, "가로"))
                            visited_garo[yy][xx] = new_total

    answer = min(visited_garo[len(board)-1][len(board)-1], visited_sero[len(board)-1][len(board)-1])
    return answer