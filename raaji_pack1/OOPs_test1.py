class myClass():
  def method1(self):
      print("Guru99")
  def method2(self,someString):
   print("Software Testing:" + someString)

c = myClass()
c.method1()
c.method2(" Testing is fun")

#calculator
class stud:

    # constructor
    # initialize instance variable

    def __init__(self, name,age,room,marks):
        self.name = name
        self.age  = age
        self.room = room
        self.marks = marks

    # instance Method
    def show(self):
        self.name = input("eneetr name:")
        self.age  = input("enter age")
        self.room = input("eneter room")
        self.marks = input("enter marks:")
        print('student Name details', self.name)
        print("Stduent Age:",self.age)
        print("student room:", self.room)
        print("student marks", self.marks)

        


# create object using constructor
s1 = stud('','','','')
s1.show()

#class mycalc():

 #  def __init__(self,a,b,c):
 #       self.a = a
 #       self.b = b
 #       self.c = c
  # def add1(self,a,b):
 #      c = int(a) + int(b)
 #      print("make addition: ",c)
   #def Sub1(self,a,b):
 #     c = int(a) - int(b)
#      print("make sub: ",c)
   #def mul1(self,a,b):

#      c = int(a) * int(b)
 ##     print("make mul: ",c)

#k = mycalc(a = input("enetr A:"),
  # b = input("eneter b:"))
#k.add1()
#k.Sub1()
#k.mul1()

#class mycalcderived(mycalc):
 #  def div1(self,a,b):
 #     c = int(a) / int(b)
 #     print("Division",c)
 #   pass
#k2 = mycalcderived()
#k2.div1('a','b')


#class Employee:
 #   def __init__(self, name, salary):
#        # public member
 #       self.name = name
        # private member
        # not accessible outside of a class
 #       self.__salary = salary

 #   def show(self):
 #       print("Name is ", self.name, "and salary is", self.__salary)

#emp = Employee("Jessa", 40000)
#emp.show()

# access salary from outside of a class
#print(emp.__salary)
class Circle:
    pi = 3.14

    def __init__(self, redius):
        self.radius = redius

    def calculate_area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print("Area of Rectangle :", self.length * self.width)
class squre:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print("Area of Square :", self.length * self.width)
# function
def area(shape):
    # call action
    shape.calculate_area()

# create object
cir = Circle(15)
rect = Rectangle(100, 15)
sqr = squre(100,100)
# call common function
area(cir)
area(rect)
area(sqr)


