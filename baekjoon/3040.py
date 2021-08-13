from itertools import combinations
ans=[]
for i in range(9):
    ans.append(int(input()))


combi = list(combinations(ans,7))

for unit in combi:
    sum=0
    for i in unit:
        sum+=i
    if sum ==100:
        for result in unit:
            print(result)

