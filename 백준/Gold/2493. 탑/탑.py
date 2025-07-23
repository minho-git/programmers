
def get_receiver_top_orders(heights):
    stack = []
    answer = [0] * len(heights)

    for i in range(len(heights) -1, -1, -1):

        while stack and stack[-1][1] < heights[i]:
            index = stack.pop()[0]
            answer[index] = i + 1

        stack.append([i, heights[i]])


    return answer


n = int(input())
array = list(map(int, input().split()))
orders = get_receiver_top_orders(array)

for num in orders:
    print(orders[num], end=" ")