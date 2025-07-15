def find_prime_list_under_number(M, N):
    prime = []
    # number 크기의 배열을 만든다.  다 Flase 값으로
    array = [False] * (int(N)+1)

    # 2부터 시작해서 number -1까지 반복한다.
    for index1 in range(2, int(N) + 1):
        if not array[index1]:
            prime.append(index1)
            for index2 in range(index1 * 2, int(N) + 1, index1):
                array[index2] = True


    for num in prime:
        if int(M) <= num <= int(N):
            print(num)

    return

# def find_prime_list_under_number(M, N):
#
#     for index in range(int(M), int(N)):
#         for divide_num in range(2, index):
#             if index % divide_num == 0:
#                 break
#
#         else:
#             print(index)
#
#
#     return
#

M, N= input().split(" ")
find_prime_list_under_number(M, N)
