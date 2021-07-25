number_list=[0 for a in range(0,10000)]

def check_not_self_number(num):
    result=int(num)
    num = str(num)
    if(len(num)==1):
        result += int(num)
        return result
    else:
        for i in num:
            result += int(i)
        if(result>=10000):
            return 0
        return result

for i in range(1,10000):
    number_list[check_not_self_number(i)] =1

for index,i in enumerate(number_list):
    if i ==0 :
        print (index)