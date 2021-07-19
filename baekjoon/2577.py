A=int(input())
B=int(input())
C=int(input())

M = str(A*B*C)
#How to initializaion list !!!!
result_list = [0 for i in range(10)]

for number in M:
     result_list[int(number)] +=1

for result in result_list:
    print (result)