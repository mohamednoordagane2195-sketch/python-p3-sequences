#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    for _ in range(length):
        print(a, end=" ")
        a, b = b, a + b
def print_arithmetic_progression(start, difference, length):
    for i in range(length):
        print(start + i * difference, end=" ")
def print_geometric_progression(start, ratio, length):
    for i in range(length):
        print(start * (ratio ** i), end=" ")
def print_harmonic_progression(start, difference, length):
    for i in range(length):
        print(1 / (start + i * difference), end=" ")
def print_square_numbers(length):
    for i in range(length):
        print(i ** 2, end=" ")  
def print_cubic_numbers(length):
    for i in range(length):
        print(i ** 3, end=" ")  
def print_factorials(length):
    factorial = 1
    for i in range(length):
        if i > 0:
            factorial *= i
        print(factorial, end=" ")
def print_prime_numbers(length):
    count = 0
    num = 2
    while count < length:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            count += 1
        num += 1
def print_fibonacci_with_limit(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b 
def print_arithmetic_progression_with_limit(start, difference, limit):
    current = start
    while current <= limit:
        print(current, end=" ")
        current += difference
def print_geometric_progression_with_limit(start, ratio, limit):
    current = start
    while current <= limit:
        print(current, end=" ")
        current *= ratio
def print_harmonic_progression_with_limit(start, difference, limit):
    current = start
    while 1 / current >= limit:
        print(1 / current, end=" ")
        current += difference
def print_square_numbers_with_limit(limit):
    i = 0
    while i ** 2 <= limit:
        print(i ** 2, end=" ")
        i += 1
def print_cubic_numbers_with_limit(limit):
    i = 0
    while i ** 3 <= limit:
        print(i ** 3, end=" ")
        i += 1
def print_factorials_with_limit(limit):
    factorial = 1
    i = 0
    while factorial <= limit:
        print(factorial, end=" ")
        i += 1
        factorial *= i
def print_prime_numbers_with_limit(limit):
    num = 2
    while num <= limit:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
        num += 1    
        