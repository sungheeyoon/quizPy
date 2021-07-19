import sys

N = int(sys.stdin.readline().strip())

_list = list(map(int,sys.stdin.readline().split()))[:N]

M = max(_list)
fake_average = 0
for number in _list:
    fake_average += (int(number)/M)*100

print(fake_average/N)