n=list(map(int,input("Enter the numbers: ")))
sum=int(input("Enter the sum: "))
i=0
count=0
val=0
while (val<(len(n)-1)):
	
	if(n[val]+n[i])==sum:
		if(val==i):i=i+1
		print("n[{0}]+n[{1}]".format(val,i))
		count=count+1
		
		
	if(i==(len(n)-1)): 
		val=val+1	
		i=val+1
	else: i=i+1
if(count!=0): print(count)
else: print("false")
