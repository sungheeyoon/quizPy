import math,sys
M,N =map(int,sys.stdin.readline().split())
def is_prime_number(p):
    if p==1:
        return 0
    elif(p%2==0):
        if p==2:
            return 1
        else:
            return 0

    middle_number= math.ceil(math.sqrt(p))
    
    for i in range(3,middle_number+1,2):
        if(p%i==0):
            return 0
    return 1

for i in range(M,N+1):
    if is_prime_number(i)==1:
        print (i)