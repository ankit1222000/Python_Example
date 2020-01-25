m,n=map(int,input().split(' '))
s=list(map(int,input().split(' ')))
max=0
for i in range(n):
	if(i+m>n-1):
		k=sum(s[i:])+sum(s[0:i+m-n])
	else:
		k=sum(s[i:i+m])
	if(k>max):
		max=k
		continue
print(max)