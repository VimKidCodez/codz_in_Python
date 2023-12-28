# To check wheather a number is a palindrome or not 

number = int(input('Enter number '))
reverse = 0
tmp = number

while number >0 :
    reverse = (reverse*10) + (number%10) # random algo from web
    number = number//10

print(reverse)
if int(reverse) == int(tmp):
    print("The number is palindrome")

else:
    print("The number is not a palindrome")

