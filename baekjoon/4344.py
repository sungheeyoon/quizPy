import sys

C = int(sys.stdin.readline().strip())

for student in range(0,C):
    scores = list(map(int,sys.stdin.readline().split()))
    div = scores[0]
    sum=0
    avg=0
    counter=0
    for i in scores[1:]:
        sum+=int(i)
    avg= sum/div
    for p in scores[1:]:
        if(p>avg):
            counter+=1
    
    print('%0.3f' % (counter/div*100)+"%")
