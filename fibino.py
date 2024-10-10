def fibi(n):
    fibprev = 0 
    fib = 1
    temp = 0 

    for i in range(2, n+1):
        temp = fibprev + fib
        fibprev = fib
        fib = temp

    print(fib)

    return

fibi(7)