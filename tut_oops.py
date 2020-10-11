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
    def __add__(self,other):
        return self.salary+other.salary
    
    def __repr__(self):
        return 'Employee {} , {}, {}'.format(self.fname,self.lname,self.salary)
    
    def __str__(self):
        return 'Employee name is {}'.format(self.fname)

harry=Employee('harsh','shah',40000)
rohan=Employee('rohan','agarwal',40)

### will demonstrate dunter methods or method overridding
#print(harry+rohan)## this will give error unsupported operand type(s) for +: 'Employee' and 'Employee',
# but when we add this dunter method it won't give any error
print(harry+rohan)

print(repr(harry))
print(str(harry))