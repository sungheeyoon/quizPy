word = input().strip()
word = word.upper()
word_dic={}

for letter in word:
    if letter in word_dic:
        word_dic[letter] +=1
    else:
        word_dic[letter] = 1

#if max value and key's value same  Add list Key
results = [k for k,v in word_dic.items() if max(word_dic.values()) == v]
if len(results) >1:
    print("?")
else:
    print(results[0])