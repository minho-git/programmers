# D[n] = D[n-1] + D[n-2]


#   0  1
#1  0  1
#2  1  0
#3  1  1
#4  2  1
#5  3  2
#6  5  3

# n = int(input())
#
# if n == 1:
#     print(1)
# else:
#
#     D = [0 for i in range(n+1)]
#     D[1] = 1
#     D[2] = 1
#
#     for i in range(2, n+1):
#         D[i] = D[i-1] + D[i-2]
#
#     print(D[n])

N = int(input())

D = [[0,0] for i in range(N+1)]
D[1] = [0, 1]

for i in range(2, N+1):
    D[i][1] = D[i-1][0]
    D[i][0] = D[i-1][0] + D[i-1][1]

print(D[N][0] + D[N][1])







