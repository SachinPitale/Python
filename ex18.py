
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)



def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(args):
	print "args : %r" % (args)



def print_none():
	print "i got nothing"




print_two("sac","hin")
print_two_again("pi", "tale")
print("ram")

print_none()
