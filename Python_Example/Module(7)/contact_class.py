class information:
	def __init__(self):
		self.name=""
		self.phone_number=0
		self.email=""
		
		
	def set_name(self,name,file):
		file.write(name+"\n")
		self.name=name
	def set_phonenumber(self,phone_number,file):
		file.write(phone_number+"\n")
		self.phone_number=phone_number
	def set_email(self,email,file):
		file.write(email+"\n")
		self.email=email
	
	def get_name(self,file):
		file.seek(0)
		return (file.readline())
		
	def get_phonenumber(self,file):
		
		return(file.readline())
		
	def get_email(self,file):
		
		return(file.readline())
	def __str__(self):
		return f'Name is {self.name}\nPhone Number is {self.phone_number}\nEmail is {self.email}'
def main():
	ww=open("info.txt","r+")
	
	info=information()
	name=input("Enter Name :")
	info.set_name(name,ww)
	info.set_phonenumber(input("Enter Phone Number: "),ww)
	info.set_email(input("enter email:"),ww)
	print("\n")
	print("Printing the data from file")
	print("Name is",info.get_name(ww),end="")
	print("PhoneNumber is",info.get_phonenumber(ww),end="")
	print("Email is",info.get_email(ww),end="")
	print("\n")
	print("Printing data throught str func.\n",info)	
main()	
