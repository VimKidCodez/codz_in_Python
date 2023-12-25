# To Write a program to check weather an number is prime or not
number = int(input('Enter number: '))
tmp = 0
for i in range(2,number+1):
	if number%i == 0:
		tmp = 1
		break
if tmp == 0:
	print("prime")
if tmp == 1:
	print("Not prime")

