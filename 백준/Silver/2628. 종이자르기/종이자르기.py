# 가로길이 세로길이
# 점선의 갯수
# 0 가로점선
# 1 세로점선

width, height = map(int, input().split())
N = int(input())

# 가로 길이 배열
slice_width_list = [0, width]
# 세로 길이 배열
slice_height_list = [0, height]

for i in range(N):
    slice_width, slice_height = map(int, input().split())
    if slice_width == 0:
        slice_height_list.append(slice_height)
    else:
        slice_width_list.append(slice_height)

# 오름차 순으로 정렬
slice_width_list.sort()
slice_height_list.sort()


# 최대 차이 가로 길이, 최대 차이 세로 길이 곱이 최대 넓이이다.

max_w = max(slice_width_list[i] - slice_width_list[i-1] for i in range(1, len(slice_width_list)))
max_h = max(slice_height_list[i] - slice_height_list[i-1] for i in range(1, len(slice_height_list)))

max_area = max_w * max_h
print(max_area)
