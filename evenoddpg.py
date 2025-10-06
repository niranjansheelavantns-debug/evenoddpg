def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_even_odd_prime():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    even_count = 0
    odd_count = 0
    prime_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        if is_prime(num):
            prime_count += 1

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)
    print("Prime numbers:", prime_count)

count_even_odd_prime()
