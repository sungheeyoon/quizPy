import sys
N = int(sys.stdin.readline().strip())
n_list=[int(i) for i in sys.stdin.readline().strip().split()[:N]]
n_list.sort()
M = int(sys.stdin.readline().strip())
m_list=[int(i) for i in sys.stdin.readline().strip().split()[:M]]

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if array[mid] == target:
        return 1

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for m in m_list:
   print(binary_search(n_list,m,0,len(n_list)-1))