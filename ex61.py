
class point:
  
  def assign(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def printpoint(self):
    print (self.x, self.y, self.z)


p1 = point()
p1.assign(2,3,4)
p1.printpoint()


p2 = point()
p2.assign(7,8,9)
p2.printpoint()




# function
# IT is reusable code
# it is outof the class
# we can call without using class object
# fuction does not have self argument


# method
# It is declare inside the class
# we can call the method using class object
# method always contain self arguments

def addition(a, b):
  return a + b


print (addition(6, 7))
