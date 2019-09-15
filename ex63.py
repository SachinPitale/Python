class Employee:
  def __init__(self, id, name):
    self.id = id
    self.name = name
  
  def display(self):
    print (self.id, self.name)



emp1 = Employee(105, "sachin")
emp1.display()


emp2 = Employee(106, "adam")
emp2.display()
