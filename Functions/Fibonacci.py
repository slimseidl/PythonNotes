def fibonacci(n):
    if n < 0:
        return -1
    else:
        fib = [0,1]
        for i in range(n):
            x = fib[-1] + fib[-2]
            fib.append(x)
        return fib[n]



start_num = int(input())
print(f'fibonacci({start_num}) is {fibonacci(start_num)}')