def 부분수열의합(total, index, array, count):
    global S, answer, N

 
    
    if index == len(array):
        if total == S and count > 0 :
            answer += 1
        return

    부분수열의합(total + array[index], index + 1, array, count + 1)
    부분수열의합(total, index + 1, array, count)

N, S = map(int, input().split())
answer = 0
array = list(map(int, input().split()))

부분수열의합(0, 0, array, 0)

print(answer)



