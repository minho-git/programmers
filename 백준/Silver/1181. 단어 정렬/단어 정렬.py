import sys


def merge_sort(words, start, end):
    # 길이가 1이 될때 까지
    if (end - start) == 1:
        return [words[start]]

    # 반으로 계속 쪼갠다.
    mid = (start + end) // 2
    left_words = merge_sort(words, start, mid)
    right_words = merge_sort(words, mid, end)

    left_words_start = 0
    right_words_start = 0

    result_words = []

    while left_words_start < len(left_words) and right_words_start < len(right_words):
        if len(left_words[left_words_start]) < len(right_words[right_words_start]):
            result_words.append(left_words[left_words_start])
            left_words_start += 1
        elif len(left_words[left_words_start]) == len(right_words[right_words_start]):
            if left_words[left_words_start] < right_words[right_words_start]:
                result_words.append(left_words[left_words_start])
                left_words_start += 1
            else:
                result_words.append(right_words[right_words_start])
                right_words_start += 1
        else:
            result_words.append(right_words[right_words_start])
            right_words_start += 1

    while left_words_start != len(left_words):
        result_words.append(left_words[left_words_start])
        left_words_start += 1

    while right_words_start != len(right_words):
        result_words.append(right_words[right_words_start])
        right_words_start += 1

    return result_words

N = int(input())

words = set(list())

for i in range(N):
    words.add(sys.stdin.readline().strip())

words = list(words)

words = merge_sort(words, 0, len(words))

for word in words:
    print(word)



