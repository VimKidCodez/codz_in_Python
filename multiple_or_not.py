# To write a program to find wheather a given number is a multiple of another number or not
Number = int(input("Enter number : "))
Multiple_Num = int(input("Enter multple number"))
if Number % Multiple_Num == 0:
    print("The number",Number,"is a muliple of",Multiple_Num)
else:
    print("The number",Number,"is not a muliple of",Multiple_Num)
