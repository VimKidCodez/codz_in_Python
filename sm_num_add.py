# To write a program that prints the sum of the numbers from 0 to n

n = int(input('Enter a number : '))
tmp = 0
for i in range(1,n+1):
    tmp = i+tmp
    
print("The sum of the numbers from 0 to n is : ",tmp)
