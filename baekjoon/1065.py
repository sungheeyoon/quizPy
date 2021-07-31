N = int(input())

def number_of_han(num):
    DP=[0]*3
    value =99
    if num <=99:
        value = num
    elif num>99:
        for i in range(100,num+1):
            DP[0]=i//100
            DP[1]=(i//10)%10
            DP[2]=i%10
            if DP[0]-DP[1]==DP[1]-DP[2]:
                value +=1
    return value

print(number_of_han(N))