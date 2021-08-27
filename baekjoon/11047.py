import sys

N,K =map(int,sys.stdin.readline().strip().split())
coins=[]
num=0
for i in range(N):
    coins.append(int(sys.stdin.readline().strip()))
for i in range(N - 1, -1, -1):#오름차순이므로 배열의역순부터 0까지
    if K ==0:
        break
    if coins[i]>K:
        continue
    num += K//coins[i]
    K %= coins[i]

print(num)