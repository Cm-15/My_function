def greet_user(name):
    print(f"สวัสดี, {name}!")
def calculate_rectangle_area(width, height):
    return width * height
def is_palindrome(word):
    return word == word[::-1]
def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
def power(base, exponent=2):
    return base ** exponent
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def print_base6(n):
    if n < 6:
        print(n, end="")
    else:
        print_base6(n // 6)
        print(n % 6, end="")
