import sys

N,K =map(int,sys.stdin.readline().split())
list_items=[]
tp=[]
max=0
for i in range(0,N):
   W,V= map(int,sys.stdin.readline().strip().split())
   list_items.append([W,V])

def comb(population,num):
	ans = []
	if num > len(population): return ans
	if num == 1:
		for i in population:
			ans.append([i])
	elif num>1:
		for i in range(len(population)-num+1): 
			for temp in comb(population[i+1:],num-1):
				ans.append([population[i]]+temp)

	return ans
for i in range(1,N+1):
    tp = list(comb(list_items,i))
    for items in tp:
        sum_weight=0
        sum_value=0
        for item in items:       
            sum_weight+=item[0]
            sum_value+=item[1]
        if(sum_weight<=K and sum_value>max):
            max=sum_value

print(max)
