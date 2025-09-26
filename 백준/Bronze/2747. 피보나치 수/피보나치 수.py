def fibonacci(num):
    if fibonacci_lst[num] is not None:
        return fibonacci_lst[num]

    result = fibonacci(num - 1) + fibonacci(num - 2)
    fibonacci_lst[num] = result
    return result

n = int(input())
fibonacci_lst = [None for i in range(46)]
fibonacci_lst[0] = 0
fibonacci_lst[1] = 1
fibonacci(n)
print(fibonacci_lst[n])

