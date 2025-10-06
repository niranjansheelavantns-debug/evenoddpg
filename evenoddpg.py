#write python program to check whether a number is odd or even
def count_even_odd():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)

count_even_odd()
 


