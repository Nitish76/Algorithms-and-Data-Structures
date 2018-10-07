# Uses python3
import sys
''' A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
of items assuming that any fraction of a loot item can be put into his bag.'''

''' Task: The goal of this code problem is to implement an algorithm for the fractional knapsack problem'''
''' Input format: The first line of the input contains the number n of items and the capacity W of a knapsack.
The next n lines define the values and weights of the items. The i-th line contains integers vi and wi—the
value and the weight of i-th item, respectively.'''

''' Constraints: 1 <=n <= 10^3, 0<= W <= 2*10^6, 0<= vi <= 2*10^6, 0<= wi <= 2*10^6
                all numbers are integers'''

def get_optimal_value(capacity, weights, values):
    value = 0.
    valperwt = [0]*n;
    for i in range(n):                          # for loop to store value per weight of every item
      valperwt[i] = values[i]/weights[i];
    
    while capacity>0 and weights:
      i = valperwt.index(max(valperwt));
      if weights[i]<=capacity:
        capacity -= weights[i];
        value += values[i];                     # all of the remaining most valuable item can be fit
      else:
        value += (capacity*valperwt[i]);
        capacity =0;                            # a portion of the remaining most valuable item can be fit
      del valperwt[i]; del weights[i]; del values[i];       #the item that was put in the knapsack is removed from the loot
    value = round(value,4); print(value);                   # max total value of fractions of items in knapsack 
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
