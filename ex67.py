class addition:
  def add (self, a , b):
    return a + b

class substration(addition):
  
  def sub (self, a, b):
    return a - b


class multiplication(substration):
  def mul (self , a, b):
    return a * b

m = multiplication()
print (m.sub(8, 2))
print (m.add(8, 2))
print (m.mul(8, 2))   

