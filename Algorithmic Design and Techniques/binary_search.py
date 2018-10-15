# Uses python3
import sys
''' This code implements iterative binary search using the divide and conquer algorithmic technique'''

'''Task: The goal in this code problem is to implement the binary search algorithm.'''

''' Input Format: The first line of the input contains an integer n and a sequence a0 < a1 < . . . < an−1
of n pairwise distinct positive integers in increasing order. The next line contains an integer k and k
positive integers b0, b1, . . . , bk−1.'''

'''Constraints: 1 <= n,k <= 10^4, 1 <= ai, bi <= 10^9'''
'''Output format: For all i from 0 to k − 1, output an index 0 <= j <= n − 1 such that aj = bi or −1 if there
is no such index.'''

def binary_search(a, x):
    left, right = 0, len(a)-1;
    while left<=right:                         
        mid = left + (right - left)//2;
        if x==a[mid]:
            return mid
        elif x<a[mid]:
            right = mid-1;
        else:
            left = mid +1;
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
