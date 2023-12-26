# Write a program to find wheather a year is leap nor not

year = int(input('Enter year: '))
if (year%4) == 0:
	print("It is leap year.")
else:
	print("It is not leap year.")