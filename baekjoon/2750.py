import sys

N = int(sys.stdin.readline().strip())
_list=[]
for i in range(0,N):
    _list.append(int(sys.stdin.readline().strip()))
_list.sort()

for i in _list:
    print(i)