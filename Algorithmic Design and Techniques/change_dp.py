# Uses python3
import sys

def get_change(m):
    mincoins = [m+1]*(m+1);
    mincoins[0] = 0;
    coins = [1,3,4]; 
    for i in range(1,m+1):
        for j in coins:
            if i>=j:
                numcoins = mincoins[i-j]+1;
            if numcoins < mincoins[i]:
                mincoins[i] = numcoins;
                
            
    #write your code here
    return mincoins[m]
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
