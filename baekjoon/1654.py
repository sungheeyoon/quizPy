import sys
K,N = map(int,sys.stdin.readline().strip().split())
lan_list = [int(sys.stdin.readline()) for _ in range(K)]

start, end =1, max(lan_list)
while(start<=end):
    middle = (end+start)//2
    result =0
    for i in lan_list:
        result+=i//middle
    
    if result >=N:
        start = middle+1
    elif result < N:
        end = middle-1
print(end)