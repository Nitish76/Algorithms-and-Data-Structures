# Uses python3

''' This program computes the sum of two single digit integers''' 

import sys

input = sys.stdin.read()  # input statement
tokens = input.split()    # storing integers in a list

a = int(tokens[0])
b = int(tokens[1])
print(a + b)
