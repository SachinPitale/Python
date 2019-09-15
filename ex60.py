class car:
  def __init__(self, speed, color):
    self.__speed = speed
    self.__color = color

  def set_speed(self, value):
    self.__speed = value

  def get_speed(self):
    return self.__speed

honda = car(200, 'green')


honda.set_speed(300)
print (honda.get_speed())













