from collections import Counter

s = input()
s = s.upper()

arr = list(Counter(s).items())
arr.sort(key=lambda x : x[1])

if len(arr) == 1:
    print(arr[-1][0])
else:
    if arr[-1][1] == arr[-2][1]:
        print("?")
    else:
        print(arr[-1][0])