#dictonay

a = {'a':1,'b':2,'c':3}

print a 


#add or change the item from dict


a['d'] = 4
print a

a['d'] = 12
print a


#remove item of dict

del a['c']

print a

#get the len of dict

lenth = len(a)
print lenth

#check membership in dict

if "b" in a:
  print "b is present"

if "c" not in a:
  print "c is not preset in a"



# delete all item form dict

a.clear()
print a

#delete the dict

del a

