n=int(input("Enter a number:"))
number=0
final=0
while(n>0):
    digit=n%10
    number=number*10+digit
    n=n//10

while(number>0):
    digit=(number%10)+1
    final=final*10+digit
    number=number//10
print("The number+1 is %d"%(final))
