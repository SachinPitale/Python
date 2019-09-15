
from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

current_file = open(input_file)

print_all(current_file)

def rewind(f):
	f.seek(0)

rewind(current_file)

print "Let's print first 3 lines"


def print_a_line(line_count, f):
	print line_count, f.readline()

current_line = 1
print_a_line(current_line, current_file)


current_line = current_line + 1
print_a_line(current_line, current_file)


current_line = current_line + 1
print_a_line(current_line, current_file)
