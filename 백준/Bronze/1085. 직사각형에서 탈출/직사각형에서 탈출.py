x, y, w, h = map(int, input().split())

answer = min(w - x, h - y, x, y)

print(answer)