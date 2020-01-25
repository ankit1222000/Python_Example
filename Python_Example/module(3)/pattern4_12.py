#Diamond 
row=int(input("Enter the Row: "))
space=row-1
star=1
i=1
while(i<=(row//2)+1):
	j=1
	while(j<=space):
		print(" ",end='')
		j=j+1
	j=1
	while(j<=star):
		print("*",end='')
		j=j+1
	print()
	space=space-1
	i=i+1
	star=star+2

space=space+2
star=star-4
while(i<=row):
	
	j=1
	while(j<=space):
		print(" ",end='')
		j=j+1
	j=1
	while(j<=star):
		print("*",end='')
		j=j+1
	print()
	i=i+1
	star=star-2
	space=space+1
if(row%2==0): 
	
	j=1
	while(j<=space):
		print(" ",end='')
		j=j+1
	
	print("*",end='')

	