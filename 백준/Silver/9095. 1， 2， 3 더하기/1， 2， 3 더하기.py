def 합계구하기(total, num):
    global count
    if total == num:
        count += 1
        return
    
    if total > num:
        return


    합계구하기(total + 1, num)
    합계구하기(total + 2, num)
    합계구하기(total + 3, num)

T = int(input())

for i in range(T):
    count = 0

    number = int(input())
    
    합계구하기(0, number)

    print(count)
    






