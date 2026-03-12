from collections import Counter

s = input()
s = s.upper()

arr = list(Counter(s).most_common(2))

if len(arr) == 1:
    print(arr[0][0])
else:
    if arr[0][1] == arr[1][1]:
        print("?")
    else:
        print(arr[0][0])