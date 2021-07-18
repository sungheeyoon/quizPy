a =int(input())
b =int(input())


first_keyword = b%10
second_keyword = b%100-first_keyword
third_keyword = b-second_keyword-first_keyword

first_answer = a*first_keyword
second_answer = (a*second_keyword)//10
third_answer = (a*third_keyword)//100
print(f"{first_answer}\n{second_answer}\n{third_answer}\n{a*b}")
