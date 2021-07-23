N = int(input())
box = 0
while(True):
    if(N%5==0):
        print(box+N//5)
        break
    elif(N<0):
        print(-1)
        break
    N-=3
    box+=1