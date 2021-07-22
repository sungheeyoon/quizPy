import sys

T = int(sys.stdin.readline().strip())

for case in range(0,T):
    R,S = map(str,sys.stdin.readline().split())
    result=""
    for i in S:
        for x in range(0,int(R)):
            result+=i

    print(result)