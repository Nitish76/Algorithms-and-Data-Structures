# Uses python3
import sys
''' Task: Given two integers a and b (both are not 0), find their greatest common divisor.'''
''' A program to compute the gcd using the Euclidean algorithm of two given integers using recursion'''

'''constraints: 1 <= a,b <= 2*10^9'''

def gcd_naive(a, b):
    if b == 0:
      return a                          # 0 is divisible by any integera
    r= a%b;
    return gcd_naive(b,r)
    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
