from sys import argv
from os.path import exists


script, from_file, to_file = argv

in_file = open(from_file)
indata= in_file.read()


print "The input file is %d bytes long " % len(indata)
print "does output %d file is exists " % exists(to_file)

print "If you want continue then press enter or ctrl-c"
raw_input()

out_file = open(to_file, 'a')
out_file.write(indata)

print "alright all done "

out_file.close()
in_file.close()

