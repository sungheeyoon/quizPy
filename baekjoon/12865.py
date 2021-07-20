import sys
from itertools import combinations

N,K =map(int,sys.stdin.readline().split())
list_items=[]
tp=[]

for i in range(0,N):
   W,V= map(int,sys.stdin.readline().strip().split())
   list_items.append([W,V])



for i in range(1,N+1):
    tp += list(combinations(list_items,i))
sum_weight_value=[[0,0]]

for items in tp:
    sum_weight=0
    sum_value=0
    for item in items:       
        sum_weight+=item[0]
        sum_value+=item[1]
    sum_weight_value.append([sum_weight,sum_value])
result=[]
for sums in sum_weight_value:
    if(sums[0]<=K):
        result.append(sums[1])

print(max(result))
