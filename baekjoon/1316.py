# import sys

# N = int(sys.stdin.readline().strip())
# result = 0
# for i in range(0,N):
#     word = sys.stdin.readline().strip()
#     check_list=[]
#     for j in range(0,len(word)-1):
#         if word[j]==word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             result-=1
#             break
# print(result)

n=int(input())
for _ in range(n):
    word=input()
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                n-=1
                break
print(n)