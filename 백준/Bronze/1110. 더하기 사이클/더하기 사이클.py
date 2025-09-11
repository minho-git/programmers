N = int(input())
cycle = 0
start = N

while True:
    # if N < 10: # 1
    #     N *= 10 # 10

    일의자리 = N % 10 # 0
    십의자리 = (N // 10)  # 1

    새로운십의자리 = 일의자리  # 0
    새로운일의자리 = ((십의자리 + 일의자리) % 10) #1

    새로운수 = (새로운십의자리 * 10) + 새로운일의자리 #
    cycle += 1 #

    if 새로운수 == start: #
        break

    N = 새로운수 #


print(cycle)