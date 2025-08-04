from collections import deque

def solution(string):

    min_length = len(string)

    for i in range(1, len(string) // 2 + 1):
        queue = deque(string[i:])
        count = 1
        answer = ""
        compare = string[:i]

        while queue:
            tmp = ""

            for j in range(i):
                if not queue:
                    break
                tmp += queue.popleft()


            if compare == tmp:
                count += 1
            else:

                if count == 1:
                    answer += compare
                else:
                    answer += str(count) + compare

                compare = tmp
                count = 1

        if count > 1:
            answer += str(count) + compare
        else:
            answer += compare

        if min_length > len(answer):
            min_length = len(answer)


    return min_length






