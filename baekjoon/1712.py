import sys

A,B,C = map(int,sys.stdin.readline().split())

if (B>=C):
        print(-1)
else:
    result = A//(C-B) +1
    print (result)
    # you can make code easier
    # while(1):
    #     if (A+B*X-C*X <0):
    #         print(X)
    #         break
    #     else:
    #         X+=1