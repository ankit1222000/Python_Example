#Plus Star Pattern
f=int(input("Enter Starts: "))
level=(f*2)+1
for i in range(level):
	if(i==f):
		
		for a in range(level):
			print("*",end=" ")
	for x in range(level):
		if(x==f and i!=f):print("*",end=" ")
		else: print(" ",end=" ")
	print()
	x=0