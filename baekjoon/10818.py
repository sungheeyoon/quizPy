numbers = int(input ())
number_list = list(map(int,input().split()[:numbers]))
max_number = number_list[0]
min_number = number_list[0]
for number in number_list:
    if(max_number <= number):
        max_number = number
    if(min_number >= number):
        min_number = number

print("%d %d" % (min_number, max_number))
