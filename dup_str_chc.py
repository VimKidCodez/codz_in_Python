string = "ABBCVB" 
tmp = string[0] 
for i in range(1,len(string)+1): 
	if tmp == i :
		print("duplicate is ",string[i])
