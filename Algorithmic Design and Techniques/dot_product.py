#Uses python3
import sys
''' You have n ads to place on a popular Internet page. For each ad, you know how
much is the advertiser willing to pay for one click on this ad. You have set up n
slots on your page and estimated the expected number of clicks per day for each
slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.'''

''' Task: Given two sequences a1, a2, . . . , an (ai is the profit per click of the i-th ad) and b1, b2, . . . , bn (bi is
the average number of clicks per day of the i-th slot), we need to partition them into n pairs (ai, bj)
such that the sum of their products is maximized.'''

''' Input format: The first line contains an integer n, the second one contains a sequence of integers
a1, a2, . . . , an, the third one contains a sequence of integers b1, b2, . . . , bn.'''

''' Constraints: 1 <= n <= 10^3, -10^5 <= ai,bi <= 10^5 for 1<= i <= n'''


def max_dot_product(a, b):
    a= sorted(a); b = sorted(b);
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res                          # max value of product

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
