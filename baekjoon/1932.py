n = int(input())
array = [[0] * n for _ in range(n)] # 0으로 전부 채워진 이차원 배열 생성
for i in range(n):
  input_data = list(map(int, input().split()))
  for j in range(len(input_data)):
    array[i][j] = input_data[j]
 
for i in range(1, n):
  for j in range(n):
    if j == 0: # 0번째 열 인경우 
      array[i][j] += array[i-1][j]
    else: # 그 외의 
      array[i][j] += max(array[i-1][j-1], array[i-1][j])
 
answer = 0
for i in range(n):
  answer = max(answer, array[n-1][i])
print(answer)        
