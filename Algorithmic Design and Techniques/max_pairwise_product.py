# Uses python3
n = int(input())
a = [int(x) for x in input().split()]

result = 0

b= sorted(a)
result = b[-1]*b[-2]
print(result)
