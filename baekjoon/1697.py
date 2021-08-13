from collections import deque
def bfs():
     ans = -1 
     que = deque() 
     que.append(n) 
     while que:
          ans+=1 
          for _ in range(len(que)):
            x = que.popleft() 
            if x == k: 
                   return ans 
            for i in (x-1, x+1, x*2):
                 if 0<=i<=100000 and num[i]==0:
                      num[i]=1 
                      que.append(i) 
                      
n, k = map(int, input().split()) 
num = [0]*100001 
num[n]=1 
print(bfs())
