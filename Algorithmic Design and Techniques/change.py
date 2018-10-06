# Uses python3
import sys

def get_change(m):
    coins = [10, 5, 1]; rm = m; n = 0;
    for i in coins:
      q = rm//i; rm = rm%i;
      n += q;
 
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
