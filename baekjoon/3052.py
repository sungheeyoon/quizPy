import sys

input_list =[]
results=[]
new_results=[]

for number in range(0,10):
    input_list += map(int,sys.stdin.readline().split())

for i in input_list:
   results.append(int(i)%42)

for offset in results:
    if offset not in new_results:
        new_results.append(offset)
print(len(new_results))