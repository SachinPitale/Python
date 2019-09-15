print "let's practice everything "
print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'


poem  = """ 
HI\n \t i am sachin \n Linux admin
"""
print poem

five = 10 -2 +3 - 6
print "your calculation is %d" %(five)


def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100 
	return jelly_beans, jars, crates



start_point= 1000
beans, jars, crates = secret_formula(start_point)

print "With a starting poin  of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10


print "we can do also these way"

print "we'd have %d beans, %d jars, and %d crates" % secret_formula(start_point) 
