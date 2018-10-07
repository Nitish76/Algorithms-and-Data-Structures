# Uses python3
import sys
''' A program to calculate change using elementary greedy algorithm'''
'''Task: The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.'''

''' Constraints: 1 <= m <= 1000'''

def get_change(m):
    coins = [10, 5, 1]; rm = m; n = 0;
    for i in coins:
      q = rm//i; rm = rm%i;                 #greedy choice
      n += q;
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
