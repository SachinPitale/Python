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



def sub(a, b):
  return a - b


print (sub(24, 2))
