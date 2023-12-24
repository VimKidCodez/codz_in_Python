#To write a program that printd the sum of number from i to  n only if it was a multile of 3 and 4

n = int(input("Enter number "))
tmp = 0
for i in range(1,n+1):
    tmp += i
    if tmp % 3 == 0 and tmp % 4 ==0:
        print("Yes",tmp)


