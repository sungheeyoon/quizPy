# import sys

# N = int(sys.stdin.readline().strip())
# input_list=[]
# for i in range(0,N):
#     input_list += map(int,sys.stdin.readline().strip())

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# sort_list = quick_sort(input_list)

# for i in sort_list:
#     print(i)

import sys
n = int(sys.stdin.readline().strip())
cnt = [0 for i in range(10000+1)]
for i in range(n):
    cnt[int(sys.stdin.readline().strip())] += 1
for i in range(1, 10000+1):
    for j in range(cnt[i]):
        sys.stdout.write(f"{i}\n")