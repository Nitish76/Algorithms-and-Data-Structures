# Uses python3

''' Task: Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number'''
''' A simple and efficient program that computes the last digit of the nth fibonacci number.
    Note that the code does not use recusrion which would waste
    memory due to multiple function calls'''
''' Constraint - 0 <= n <= 10.0e+7'''

import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    
    # the following loop adds only the units digit of 2 consecutive fibonacci numbers
    for _ in range(n - 1):                                  
        previous, current = current%10, (previous + current)%10

    return current % 10

# input output statements
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
