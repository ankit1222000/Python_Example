n=int(input("Enter a number:"));
number=0
while(n>0):
    digit=n%10
    number=number*10+digit
    n=n//10


print("The reversed of digits is:",number)