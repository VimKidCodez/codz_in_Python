# Write a program to print the following pattern

"""1
22
333
4444
55555"""

for i in range(0,5+1):
    for j in range(1,i+1):
        print(i,end="")
    print("")
