# Uses python3
import sys
''' Task: Given two integers a and b, find their least common multiple.'''

'''The least common multiple of two positive integers a and b is the least positive
integer m that is divisible by both a and b. This program computes the lcm using recursion'''

'''Constraints: 1 <= a,b <= 2*10^9'''

def gcd_naive(a, b):
    if b == 0:
      return a                              # 0 is divisble by any integer
    r= a%b;
    return gcd_naive(b,r)                   # First the gcd is found

def lcm_naive(a,b):
    lcm = int(a*b//gcd_naive(a,b));         # lcm = product of integers/gcd
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
