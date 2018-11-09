# Uses python3
import sys
''' You are given a primitive calculator that can perform the following three operations with
the current number x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is given a
positive integer n, find the minimum number of operations needed to obtain the number n
starting from the number 1.'''

'''Input format: A single integer n'''
'''Output format: The first line, outputs the minimum number k of operations needed to get n from 1.
The second line outputs a sequence of intermediate numbers. That is, the second line contains
positive integers a0, a2, . . . , ak−1 such that a0 = 1, ak−1 = 𝑛 and for all 0 ≤ i < k − 1, ai+1 is equal to
either ai + 1, 2ai, or 3ai. If there are many such sequences, any one of them is output.'''

'''Constraint: 1 <= n <= 10^6'''


def prim_cal(n):
    if n == 1:
        return 0, [1]
    minops = [n]*n; minops[0] = 0;
    opt = []; i=1
    while i<n:
        if (i+1)%3 == 0:
            m1 = minops[(i+1)//3 - 1] + 1;
        else: m1 = n+2;
        if (i+1)%2 == 0:
            m2 = minops[(i+1)//2 - 1] + 1;
        else: m2 = n+2;
        m3 = minops[i-1] + 1;
        minops[i] = min(m1,m2,m3);
        i += 1;
    m=minops[-1]; opt.append(n); j=n-1;
    while len(opt)<=m:
        if (j+1)%3==0 and minops[j]-1 == minops[(j+1)//3 - 1]:
            opt.append((j+1)//3); j = (j+1)//3 - 1
        elif (j+1)%2==0 and minops[j]-1 == minops[(j+1)//2 -1]:
            opt.append((j+1)//2); j = (j+1)//2 - 1
        else:
            opt.append(j); j = j-1;
        
    #if opt[-1]!= 1: opt.append(1);
    opt.reverse();
    return m, opt
input = sys.stdin.read()
n = int(input)
m, opt = prim_cal(n);
print(m)
for x in opt:
    print(x, end=' ')
