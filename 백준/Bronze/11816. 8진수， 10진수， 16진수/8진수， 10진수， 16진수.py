num = input()

if num[0] == '0':
    if num[1] == 'x':
        num = num[2:]
        print(int(num, 16))
    else:
        num = num[1:]
        print(int(num, 8))

else:
    print(num)