#Hollow Triangle
level=int(input("Enter Level: "))
space=level-1
for i in range(1,level):
	j=1
	while(j<=space):
		print(" ",end='')
		j=j+1
	j=1
	for j in range(1,i*2):
		if((j==1)or (j==(i*2-1))): print("*",end='')
		else : print(" ",end='')
		j=j+1
	print()
	space=space-1
	i=i+1
for i in range(level) : 
	print ('*', end =' ') 
			
