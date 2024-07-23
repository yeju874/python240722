# Class1.py

class Person:
    def __init__(self):
        self.name = "default name"
    def print(self):
        print ("My name is {0}".format(self.name))

p1 = Person()
p1.print()
p2 = Person()
p2.name = "yeju"
p2.print()


#전역변수
strname = "전역변수의 값"
class DemoString:
    def __init__(self):
        self.strname =""
    def set(self, msg):
        self.strname = msg
    def print(self):
        print(self.strname)

g = DemoString()
g.set("멤버변수 셋팅")
g.print()

class BankAccount:
    def __init__(self, id, name, balance):
        #클래스 내부에서만 접근할수 있도록 __ 추가 필요 (이름숨김)
        self.__id = id
        self.__name = name
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} ,{1}, {2}".format(self.__id, self.__name, self.__balance)

account1 = BankAccount(100, "yeju", 15000)
account1.withdraw(5000)
print(account1)

#클래스 외부 접근
#print(account1.__balance)
class Person : 
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber
    def printInfo(self):
        print("Info(Name : {0}, Phone number : {1})".format(self.name, self.phonenumber))

class Student(Person):
    def __init__(self, name, phonenumber, subject, studentID):
        Person.__init__(self, name, phonenumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("Info(Name : {0}, Phone number : {1})".format(self.name, self.phonenumber))
        print("Info(Subject : {0}), studentID : {1})".format(self.subject, self.studentID))
    

P = Person("yeju", "010-2622-2222")
S = Student("yeji", "010-1111-1111", "전자", "100")

P.printInfo()
S.printInfo()
