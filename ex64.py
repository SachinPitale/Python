class student:
  def __init__(self, name):
     self.name = name
     

  def show(self):
    print ("hello",self.name )

s1 = student("john")
s1.show()
