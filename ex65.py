class student:
  def __init__(self,name,id,age):
    self.name = name
    self.id = id
    self.age = age
  
  def show(self):
    print (self.name, self.id, self.age)



s1 = student("john", 101, 22)
s1.show()
# Print the attribute name of the objects
print (getattr(s1,'name'))
print (getattr(s1,'id'))

# reset the value of attribute 

setattr(s1,"age",23)

print (getattr(s1,'age'))
# hasattr built in class : It returns true if the object contains some specific attribute.

print (hasattr(s1,'id'))

# deletes the attribute age

#delattr(s1,'id')

s1.show()















