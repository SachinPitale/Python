from sys import argv
script, user_name = argv
prompt = '> '
print " Hi %s i'm the %s script. " % (user_name, script)
print "i'd like to ask few question"
print "do you like me %s " % user_name
likes = raw_input(prompt)

print  "where do you leave %s " % user_name
lives = raw_input(prompt)

print "What kind of computer do you have",
computer = raw_input(prompt)

print """ 
Alright so you said %r about linking me.
you live in %r not sure where that is
and you have a %r computer. nice

""" % (likes, lives, computer )
