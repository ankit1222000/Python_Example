from parent import automobile
class car(automobile):
 
 def __init__(self,__doors,__make,__model,__mileage,__price):
  automobile.__init__(self,__make,__model,__mileage,__price)
  self.__doors=__doors
 def set_doors(self,doors):
  self.__doors=doors
 def get_doors(self):
  return self.__doors

class truck(automobile):
 
 def __init__(self,__drive,__type,__make,__model,__mileage,__price):
  automobile.__init__(self,__make,__model,__mileage,__price)
  self.__drive=__drive
  self.__type=__type
 def set_drive(self,drive):
  self.__drive=drive
 def get_drive(self):
  return self.__drive
 def set_type(self,type):
  self.__type=type
 def get_type(self):
  return self.__type

class suv: 
 def __init__(self,__pas,__cap,__make,__model,__mileage,__price):
  automobile.__init__(self,__make,__model,__mileage,__price)
  self.__pas=__pas
  self.__cap=__cap
 def set_pas(self,pas):
  self.__pas=pas
 def get_pas(self):
  return self.__pas
 def set_cap(self,cap):
  self.__cap=cap
 def get_cap(self):
  return self.__cap



def main():
 swift=car("2","indian","2010","500","1000000")
 swift.set_doors(input("set doors: "))
 print("Doors: ",swift.get_doors())
 
 mahindra=truck("Road","automatic","indian","2010","500","1000000")
 mahindra.set_drive(input("set drive: "))
 print("Drive: ",mahindra.get_drive())
 mahindra.set_type(input("set type: "))
 print("Type: ",mahindra.get_type())
 
 bolero=suv("expired","blue","indian","2010","500","1000000")
 bolero.set_pas(input("set pass: "))
 print("Pass: ",bolero.get_pas())
 bolero.set_cap(input("set cap: "))
 print("Type: ",bolero.get_cap())

main()

	