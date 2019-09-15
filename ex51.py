#set datatype


x = {1,2,3,4,5,6,7,8,9}
print x

#add method to add the item in set 

x.add(15)
print x

#remove method to remove the item from set

x.remove(9)
print x

#len method to get of the set

lenth=len(x)
print lenth



#check the membership in x


if 5 in x:
  print "True"


if 9 not in x:
  print "falue"



#clear method 
#delete the all item from set

x.clear()
print x
