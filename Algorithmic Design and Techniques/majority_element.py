# Uses python3
import sys
''' An algorithm to find if a majority element exists in an array using divide-and-conquer'''

''' Input format: The first line contains an integer n, the next one contains a sequence of n non-negative
integers a0, a1, . . . , an−1.'''

'''Output Format: Output 1 if the sequence contains an element that appears strictly more than n/2 times,
and 0 otherwise.'''

'''Constraints: 1 <= n <= 10^5, 0 <= ai <= 10^9'''

def maj(a):
    if len(a)==1:
        return a[0]
    mid= len(a)//2;
    ele_l =maj(a[:mid]);
    ele_r =maj(a[mid:]);
    if ele_l==ele_r:
        return ele_l
    lc,rc = 0,0;
    lc = a.count(ele_l);
    rc = a.count(ele_r);
    if lc>=mid+1:
        return ele_l
    elif rc>=mid+1:
        return ele_r
    else:
        return None
    
def getm(a):
    if maj(a):
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(getm(a));
