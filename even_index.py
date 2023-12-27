# To write a program that prints the index that is even
string = "hello"
# Lenght of string
lenght = len(string)

for i in range(0,lenght+1):
    if i % 2 == 0:
        print(string[i])
