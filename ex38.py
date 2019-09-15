ten_things = "apple mongo orange jackfriut sugar tomato"

print "there are not 10 things let  me complete first"

stuff= ten_things.split(' ')
more_stuff = ["day", "night", "song","Frisbee", "corn","banana","boy","girl"]

while len(stuff) != 10 :
	next_one = more_stuff.pop()
	print "adding new", next_one
	stuff.append(next_one)
	print "There's %d items now. " % len(stuff)
	
	
	
print "print all stuff", stuff

print stuff[1]

print stuff[-1]
print stuff.pop()
print '  '. join(stuff)


print '# '. join(stuff[3:5])
