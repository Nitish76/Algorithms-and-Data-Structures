# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    a,b,i = 0,1,0
    while i<n:
     a,b = b, a+b;
     i+=1;
    return a

n = int(input())
print(calc_fib(n))
