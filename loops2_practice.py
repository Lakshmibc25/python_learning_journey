n = int(input("enter a number:"))

for i in range(1, n+1):
    print("*" * i)

num = int(input("enter a number:"))
reverse =0

while num >0:
    digit = num %10
    reverse = reverse * 10 + digit
    num = num //10
print("reversed number:",reverse)

num = (input("enter your number : "))
even_count = 0
odd_count =0

for digit in num:
    if digit.isdigit():
        if int(digit)%2 == 0:
            even_count +=1
        else:
            odd_count +=1
print("even digit:",even_count)
print("odd digits",odd_count)


for i in range(1,11):
    num = i*i
    print(num)






