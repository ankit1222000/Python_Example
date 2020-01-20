price=99
discount=0
package=int(input("Enter the number of packages: "))

def amount(discount):
    total=(price*package)-((price*package)*(discount/100))
    print("dicount given is {0}% and the total amount is {1}".format(discount,total))

if(package>=10 and package<=19):
    discount=10
    amount(discount)
    
elif package>=20 and package<=49: 
    discount=20
    amount(discount)
elif package>=50 and package<=99:
    discount=30
    amount(discount)
elif package>=100:
    discount=40
    amount(discount)
else:
    total=price*package
    discount="0"
    print("dicount given is {0}% and the total amount is {1}".format(discount,total))