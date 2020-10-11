class Employee:
    increment=1.5
    no_of_employee=0
    #instance
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
        Employee.no_of_employee+=1

    def increase(self):
        ## why do we use self?
        #pass
        self.salary=self.salary*self.increment
        
    @classmethod
    def change_increment(cls,amnt):
        cls.increment=amnt
    
    @classmethod
    def frm_str(cls,emp_str):
        fname,lname,salary=emp_str.split("-")
        return cls(fname,lname,salary)
    
    @staticmethod
    def is_open(day):
        if day=="sunday":
            return False
        else:
            return True
    #pass if class does not do anything we should use 
#harry=Employee()
#larry=Employee()

#harry.salary=3000
#larry.name="larry"
 ###but to resuse code we have written class so will make constructors to reuse class
print(Employee.no_of_employee)
## harry and larry is object
harry=Employee('harry','singh',40000)
print(Employee.no_of_employee)
larry=Employee('larry','jackson',30000)
print(Employee.no_of_employee)
jerry=Employee('jerry')## it requires all argument
print(harry.salary,larry.lname)
 ### we can add new 
harry.increment=9
print(harry.__dict__)## this helps us to view all attributes of object harry
 #why do we use self?
 ### here if we call 
 #harry.increase()
 ## if self not written in increase function this will give error
 #TypeError: increase() takes 0 positional arguments but 1 was given
 ### using class method
 ### if we don't specify self in return of increment it will first search if the variable exits in instane 
 ## if not then will search in class we can either write Employee.increment if write self.increment and self.increment=1.4
 ## written in __init__ inscatance then it will take the value written in __init__ instance 
print(harry.__dict__)
harry.increase()
print(harry.__dict__)
 
### class method demo
print(harry.salary)
Employee.change_increment(4)
harry.increase()
print(harry.salary)

#Class Methods As Alternative Constructor, but init will be still required
rohan=Employee.frm_str("rohan-roy-30000")
print(rohan.fname)

### If we don't require either class methods or class attributes so we just can use functions of class
## by using staticmethod
print(Employee.is_open("monday"))
print(Employee.is_open("sunday"))

###Inheritance
class Programmer(Employee):
    def __init__(self,fname,lname,salary,prolang,exp):
        super().__init__(fname,lname,salary)
        self.prolang=prolang
        self.exp=exp
    def increase(self):
        self.salary=(self.salary*(self.increment+0.2))
        return self.salary
harsh=Programmer('harsh','shah',4000,'python',5)
print(harsh.exp)
print(harsh.increase())
print(harsh.salary)

"""
what is self?
The self is used to represent the instance of the class. With this keyword,
 you can access the attributes and methods of the class in python.
 It binds the attributes with the given arguments

"""
help(Programmer)# it gives details of the class



















