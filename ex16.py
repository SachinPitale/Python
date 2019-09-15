from sys import argv

script, filename = argv
print "we are going to erase %r " % filename
print "if you don't want that hit ctrl+c"
print "If you do want hit enter "

raw_input("?")
print "opening the file ..."
target = open(filename, 'a')

print "turncating the file. goodbay "
target.truncate()

print "now i am going to ask three lines"

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

target.write(line1)
target.write("\n")


target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "finally we close it "
target.close()
