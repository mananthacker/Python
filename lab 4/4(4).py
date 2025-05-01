def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(n))
        temp //= 10
    return sum == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n ** 2
    return str(n) in str(square)


n = int(input("Enter a number: "))


print(f"Is prime: {is_prime(n)}")
print(f"Is perfect: {is_perfect(n)}")
print(f"Is armstrong: {is_armstrong(n)}")
print(f"Is palindrome: {is_palindrome(n)}")
print(f"Is automorphic: {is_automorphic(n)}")
