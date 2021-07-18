number_list =[]
for i in range(0,9):
    number_list += map(int,input().split("\n"))
    
max_number=number_list[0]
max_index = 0

for index, number in enumerate(number_list):
    if(number>=max_number):
        max_number=number
        max_index=index+1

print(max_number)   
print(max_index)