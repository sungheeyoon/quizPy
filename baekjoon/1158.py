N, K = map(int, input().split())
 
circle = [i for i in range(1, N+1)]
 
result = []
delete= K-1
while len(circle):
    if delete >= len(circle):
        delete = delete % len(circle)
    else:
        result.append(str(circle.pop(delete)))
        delete += (K-1)
 
print("<", ", ".join(result), ">", sep='')