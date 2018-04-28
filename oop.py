#creating class and object in python
class Animal:
  #class attribute
  species="mammal"
  #instance attribute
  def __init__(self,name,weight):
    self.name=name
    self.weight=weight
  #instance method
  def king(self,yn):
    print("{} is {} king".format(self.name,yn))
#instaite the object
lion=Animal("lion",500)
tiger=Animal("tiger",200)
print("{} is {} kg weight".format(lion.name,lion.weight))
lion.king("yes")

#inheritance
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


#polymorphism
class Lion:
  def eat(self):
    print ("lion eat flesh")
  def swim(self):
    print ("can swim")
class Rabbit:
  def eat(self):
    print ("eats green vegetables")
  def swim(self):
    print("cannot swim")
def swimtest(animal):
  animal.swim()
rab=Rabbit()
swimtest(rab)























