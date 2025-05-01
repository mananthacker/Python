def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example: Generate the first 10 Fibonacci numbers
n = 10
fibonacci_numbers = generate_fibonacci(n)
print(fibonacci_numbers)
