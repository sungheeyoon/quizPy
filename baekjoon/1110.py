number = int(input())

if (number<10):
    number *= 10

cycle = 1
cycle_number =number
while(1):
    ten = cycle_number//10
    unit = cycle_number%10 
    result = unit*10+((ten+unit)%10)
    if(number == result):
        print(cycle)
        break
    else:
        cycle +=1
        cycle_number = result
