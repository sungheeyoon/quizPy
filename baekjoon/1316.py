import sys

N = int(sys.stdin.readline().strip())
input_list=[]
for i in range(0,N):
    input_list.append(str(sys.stdin.readline().strip()))

print(input_list)

def group_word_check(word):
    for unit in word:
        print(unit)
        ###need think