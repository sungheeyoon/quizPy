import sys
T = int(sys.stdin.readline().strip())

for i in range(0,T):
    input_data=sys.stdin.readline().strip()
    count =0
    for unit in input_data:
        if count <0:
            break
        if unit =="(":
            count +=1
        elif unit ==")":
            count -=1

    if count == 0:
        print("YES")
    else:
        print("NO")