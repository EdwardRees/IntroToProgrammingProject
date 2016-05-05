import time
import socket
#name = raw_input("What's your name? ")
#print ("Hello " + name + "!!!!! ")
response = raw_input("Are you ready(Y/N)? ")
newResponse = response.lower()
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])

if newResponse == "yes" or newResponse == "y" or newResponse == "ye":
    print int(3)
    time.sleep(1)
    print int(2)
    time.sleep(1)
    print int(1)
    time.sleep(1)
    print "LETS GO!"
    time.sleep(1)



    TCP_IP = '10.2.176.172'
    IP_PORT = 52391


    Sec = 0
    Min = 0
    Lap = 0



    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = client_socket.connect((TCP_IP, IP_PORT))

#school = client_socket.connect((SCHOOL_TCP_IP, SCHOOL_IP_PORT))
    while True:

        Sec += 1
        secClock = (str(Min) + " Mins " + str(Sec) + " Sec ")
        print secClock
        time.sleep(1)
        if Sec == 60:
            Sec = 0
            Min += 1
            clock = (str(Min) + " Minute")
            print(clock)


        data = client_socket.recv(1000)

        if ():
            split = data.split(',')
            axisY = split[6]
            client_socket.close()      

            break;


        else:
            
            split = data.split(',')
            split6 = (round(float(split[6]),3))
            #print "RECIEVED:" ,
            print split6


        if  float(split6) >= float(0.3):
            print("Finished");
            #client_socket.close()
            time.sleep(0.75)
            print ("Congratulations! You lasted for " + str(Sec) + " seconds long")
            break;




        if float(split6) <= float(-0.3):
            print("Finished");
            #client_socket.close()
            time.sleep(0.75)
            print ("Congratulations! You lasted for " + str(Sec) + " seconds long")
            break;




if newResponse == "no":
    #print "Have a nice day " + name + "!!"
    time.sleep(1)
    print "Bye!"

#print ("Good job " + name + "!!")
#print ("You were on for " + Sec + "seconds!!")


quit

#Key information, on the phone go to the settings and deselect all options except DM
#Then change your recording rate to 1 s
