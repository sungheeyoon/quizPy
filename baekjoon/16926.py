import sys

N,M,R = map(int,sys.stdin.readline().strip().split())

A = [[0 for i in range(M)] for j in range(N)] 

print(A)

# n, m, r = map(int, input().split(' '))
# graph = [list(map(int, input().split(' '))) for _ in range(n)]

# for _ in range(r):
#     for i in range(min(n, m) // 2):
#         s_x, s_y = i, i
#         s_value = graph[s_x][s_y]

#         for j in range(i + 1, n - i):  #��
#             s_x = j
#             prev_value = graph[s_x][s_y]
#             graph[s_x][s_y] = s_value
#             s_value = prev_value

#         for j in range(i + 1, m - i):  #��
#             s_y = j
#             prev_value = graph[s_x][s_y]
#             graph[s_x][s_y] = s_value
#             s_value = prev_value

#         for j in range(i + 1, n - i):  #��
#             s_x = n - j - 1
#             prev_value = graph[s_x][s_y]
#             graph[s_x][s_y] = s_value
#             s_value = prev_value

#         for j in range(i + 1, m - i):  #��
#             s_y = m - j -1
#             prev_value = graph[s_x][s_y]
#             graph[s_x][s_y] = s_value
#             s_value = prev_value

# for i in range(n):
#     for j in range(m):
#         print(graph[i][j], end=' ')
#     print()