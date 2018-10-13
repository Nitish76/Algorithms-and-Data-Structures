# Uses python3
import sys

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
