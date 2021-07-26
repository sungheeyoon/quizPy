import sys
T = int(sys.stdin.readline().strip())

for i in range(0,T):
    H,W,N=map(int,sys.stdin.readline().split())
    result=[0]*H*W
    index=0
    for width in range(1,W+1):
        for height in range(1,H+1):
            s_height=str(height)
            s_width=str(width)
            if(width<10):
                result[index]=s_height+"0"+s_width
                index+=1
            else:
                result[index]=s_height+s_width
                index+=1
    print(result[N-1])