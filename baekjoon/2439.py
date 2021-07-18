numbers = int(input())
for number in range(1,numbers+1):
    star=""
    for num in range(0,number):
        star +="*"
    print(star.rjust(numbers))
