import time
import socket
import datetime
import Tkinter


yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])
text_file = open("TextFile.txt", "a")
playAgain = True
answer = ''

time1 = time.time()
time2 = time.time()


Trial = True

now = datetime.datetime.now()

RED = '\033[1;31;0m'
BLUE = '\033[1;34;0m'
CYAN = '\033[1;36;0m'
GREEN = '\033[1;32;0m'
Normal = '\033[0;0;0m'



while True:

    name = raw_input("What's your name? ")
    studentid = raw_input("What is your student ID? ")
    print ("Thank you! " + "Hello! " + name + "!!!!")
    response = raw_input("Are you ready(Y/N)? ")
    newResponse = response.lower()
    #http://ozzmaker.com/add-colour-to-text-in-python/
    if newResponse == "yes" or newResponse == "y" or newResponse == "ye":
        while playAgain:

            print BLUE + str(int(3))
            time.sleep(1)
            print BLUE + str(int(2))
            time.sleep(1)
            print BLUE + str(int(1))
            time.sleep(1)
            print GREEN + "LETS GO!" + Normal
            time.sleep(1)
            time1 = time.time()


            TCP_IP = '10.2.177.212'
            IP_PORT = 60862


            Sec = 0
            Min = 0
            Lap = 0



            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            IP = client_socket.connect((TCP_IP, IP_PORT))

            while True and Trial:


                '''Sec += 1
                secClock = (str(Min) + " Mins " + str(Sec) + " Sec ")
                print secClock
                time.sleep(1)
                if Sec == 60:
                    Sec = 0
                    Min += 1
                    clock = (str(Min) + " Minute")
                    print(clock)
                    '''


                data = client_socket.recv(2000)

                if ():
                    split = data.split(',')
                    axisY = split[6]
                    client_socket.close()

                    break;


                else:

                    split = data.split(',')

                    split6 = (round(float(split[6]),3))
                    if split6 == "XArbitraryCorrectedZVertical":
                        continue
                    '''if split6 == "XArbitraryCorrectedZVertical":
                        print ("Ignore this")
                        continue
                    if split6 == int:
                        split7 = (round(float(split[6]),3))
                        time.sleep(1)
                        print split7'''
                    print split6
                    time.sleep(1)





                if  float(split6) >= float(0.3) or float(split6) <= float(-0.3):
                    print(RED + "STOP!!!");

                    time.sleep(0.5)




                    text_file.write("Student Name: " + name + "\n")
                    text_file.write("Student ID: " + studentid + "\n")
                    text_file.write("Date: " + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + " (format is Date/Month/Year)"  + "\n")
                    text_file.write("Time: ")
                    time2=time.time()
                    text_file.write(str(int(time2)-int(time1)))
                    print (BLUE + "Congratulations! You lasted for " + RED + str((int(time2) - int(time1))) + BLUE + " Seconds!" + Normal)
                    time1 = time2
                    text_file.write(" Seconds" + "\n" + "\n")
                    #text_file.close()
                    answer = raw_input('Run again? (y/n): ')
                    #if answer in ('y', 'n'):
                    #    break
                    #print 'Invalid input.'
                    if answer == 'y':
                        break
                    if answer == 'n':
                        text_file.close()
                        print 'Goodbye'
                        break
                        Trial = False

            break;




    if newResponse == "no":

        time.sleep(1)
        print "Bye!"




    quit

    #Key information, on the phone go to the settings and deselect all options except DM
    #Then change your recording rate to 1 s


    #(v)Time Balance - stop on specific value
    #reset button
    #(ignore?)Telemetry data
    #(v)student input (name and id)
    #(v)Date included in Text file


    #Different trials
