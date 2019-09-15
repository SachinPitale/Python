#class car:
#  def __init__(self): # it is constructor for this class
                      # init method is used to serve the function or method of class
                      # it usually to initialize  the same function of class 
                      # This is first method it will call when you crate the instance of class 


class car:
  def __init__(self, speed, color):
    print ('the__init__ is called')
    print (speed)
    print (color)
    self.color = color # intialize the attribute
    self.speed = speed 
ford = car(200, 'red') # when class instance it will call init method
honda = car(300, 'green')
audi = car(500, 'blue')

print (ford.color)
print (ford.speed)
