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
        #self.email=fname+lname+'@gmail.com'

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
    @property
    def email(self):
        return self.fname+self.lname+'@email.com'
    @email.setter
    def email(self,given_email):
        self.email=given_email
    
    @email.deleter
    def email(self):
        self.lname=None
        self.fname=None

if __name__=='__main__':
    harry=Employee('harsh','shah',40000)
    rohan=Employee('rohan','agarwal',40)
    #print(harry.email,rohan.email)
    #after making funtion for email
    rohan.lname='khanna'
    ## after property no use of ()
    print(harry.email(),rohan.email())
    print(harry.email,rohan.email)## after property
    
    
    
    
    
    
    
    
    
    

print(5+6)
print("5" + "6")

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

    
    