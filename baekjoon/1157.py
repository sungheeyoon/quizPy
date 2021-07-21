word = input().strip()
word = word.lower()
word_dic={}

for letter in word:
    if letter in word_dic:
        word_dic[letter] +=1
    else:
        word_dic[letter] = 1
#get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다.
print(word_dic)
max_value = max(word_dic,)