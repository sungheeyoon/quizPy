import sys

T = int(sys.stdin.readline().strip())

for case in range(0,T):
    input_case = list(sys.stdin.readline().strip())
    count_sum=0
    count=0
    for unit in input_case:
        if unit=="O":
            count +=1
            count_sum+=count
        else:
            count =0
    print(count_sum)

