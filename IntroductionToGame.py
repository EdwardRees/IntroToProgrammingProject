import time
name = raw_input("What's your name?")
print ("Hello " + name + "!!!!!")
response = raw_input("Are you ready(Y/N)?")
newResponse = response.lower()
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])

if newResponse == "yes":
    print int(3)
    time.sleep(1)
    print int(2)
    time.sleep(1)
    print int(1)
    time.sleep(1)
    print "LETS GO!"

if newResponse == "no":
    print "Have a nice day " + name + "!!"
    time.sleep(1)
    print "Bye!"

quit

