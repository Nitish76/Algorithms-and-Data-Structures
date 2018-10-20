# Uses python3
import sys
import random
''' An implementation of quick sort (3-way partition) for quickly sorting sequences 
    even when they contain many equal elements using divide-and-conquer'''

'''Input format: The first line of the input contains an integer n. The next line contains a sequence of n
integers a0, a1, . . . , an−1'''

''' Constraints: 1 <= n <= 10^5, 1 <= ai <= 10^9'''

'''Output format: Sorted sequence in non-decreasing order'''

def partition3(a, l, r):
    x=a[l];
    j,k=l,r;
    i = j;
    while i<=k:
        if a[i]<x:
            a[i], a[j] = a[j], a[i];
            j += 1
        elif a[i]>x:
            a[i], a[k] = a[k], a[i];
            i -= 1;
            k -= 1;
        i += 1;
    return j,k
            
    
  #write your code here
    

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,n = partition3(a, l, r)
    randomized_quick_sort(a, l, m-1);
    randomized_quick_sort(a, n+1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
