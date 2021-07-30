import math
import sys

N = int(sys.stdin.readline().strip())


def is_prime_number(n):
    if n == 1:
        return 0
    if n%2==0:
        if n==2:
            return 1
        else:
            return 0 
    for i in range(3,math.ceil(math.sqrt(n))+1,2):
        if(n%i==0):
            return 0
    return 1

result = 0
q = list(map(int,sys.stdin.readline().strip().split()))
for i in q:
    result+=is_prime_number(i)
print(result)