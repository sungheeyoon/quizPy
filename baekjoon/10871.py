N,X = map(int,input().split())

A = list(map(int,input().split()))[:N]
answer=""
for number in A:
    if number<X:
       answer+=str(number)+" "

print (answer)