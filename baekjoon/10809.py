import string
S = input()

#string.ascii_lowercase is A to Z string
#dict.fromkeys(seq ,value)
dic = dict.fromkeys(string.ascii_lowercase, -1)

for index,unit in enumerate(S):
    if(dic[unit] == -1):
        dic[unit] = index
result =str(dic.values())
print(result[13:-2].replace(',',''))