N = int(input())

dic = {0:0,1:1}

def factorial(n):
    if n ==0:
        return 1
    if n in dic:
        return dic[n]
    if n not in dic:
        dic[n] = n*factorial(n-1)
    return dic[n]

print(factorial(N))