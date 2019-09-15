class point:
  def __init__(self, x, y, z):
    print "class object"
    self.x = x
    self.y = y
    self.z = z

  def printpoint(self):
    print (self.x, self.y, self.z)


p1 = point(7, 8, 9)
p1.printpoint()





















