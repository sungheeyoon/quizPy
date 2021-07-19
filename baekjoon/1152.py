import sys

sentence = sys.stdin.readline().strip()

_list=sentence.split(' ')
#space!!!
if sentence =="":
    print(0)
else:
    print(len(_list))