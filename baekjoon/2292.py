N = int(input())
first=2
last=7
depth=2
idx = 12
for i in range(1,N+1):
    if(N==1):
        print(1)
        break
    if(first<=N and N<=last):
        print(depth)
        break
    depth+=1 
    first = last+1
    last = last+idx
    idx +=6
