N = int(input())

X = list(map(int,input()))[:N]
sum = 0

for i in X:
    sum +=i

print(sum)