N=int(input())
dic={0:0 , 1:1}
def fibonacci(n):
    if n in dic:
        return dic[n]
    dic[n] = fibonacci(n-1)+fibonacci(n-2)
    return dic[n]
    
print (fibonacci(N))