import sys
N= int(sys.stdin.readline().strip())
results=[0]*N
for i in range(0,N):
    results[i] = int(sys.stdin.readline().strip())
results.sort()
for result in results:
    print(result)