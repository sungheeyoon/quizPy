N = int(input())

A = list(map(int, input().split()))

count = 1
benchmark=A[0]
for i in A[1:]:
    if i > benchmark:
        benchmark=i
        count +=1
    else:
        continue

print(count)
# n=int(input())
# a=list(map(int, input().split()))

# d=[1]*n
# for i in range(1,n):
#   for j in range(i):
#     if a[j]<a[i]:
#       d[i]=max(d[i],d[j]+1)

# print(max(d))