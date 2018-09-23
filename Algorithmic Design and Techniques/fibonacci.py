# Uses python3
''' Task: Given an integer 𝑛, find the 𝑛th Fibonacci number'''
''' A simple a nd efficient program that computes the nth fibonacci number.
    Note that the code does not use recusrion which would waste
    memory due to multiple function calls'''
''' Constraint - 0 <= n <= 45'''

def calc_fib(n):
    if (n <= 1):
        return n
    a,b,i = 0,1,0           #initialing numbers to compute fibonacci numbers and a counter i
    while i<n:
     a,b = b, a+b;          # simultaneous assignment of variables for the next fibonacci number and to store the previous one
     i+=1;
    return a

n = int(input())
print(calc_fib(n))

