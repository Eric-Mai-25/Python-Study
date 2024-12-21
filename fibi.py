def generate_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Example
print(generate_fibonacci(5))  # [0, 1, 1, 2, 3]
print(generate_fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]