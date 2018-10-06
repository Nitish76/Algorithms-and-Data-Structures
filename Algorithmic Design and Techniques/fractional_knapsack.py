# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    valperwt = [0]*n;
    for i in range(n):
      valperwt[i] = values[i]/weights[i];
    #valperwt = sorted(valperwt, reverse = True);
    while capacity>0 and weights:
      #if capacity == 0:
        #return value
      i = valperwt.index(max(valperwt));
      if weights[i]<=capacity:
        capacity -= weights[i];
        value += values[i];
      else:
        value += (capacity*valperwt[i]);
        capacity =0;
      del valperwt[i]; del weights[i]; del values[i];
    value = round(value,4); print(value);
   # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
