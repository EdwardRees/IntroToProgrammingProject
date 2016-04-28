#http://www.pythonprasanna.com/Papers%20and%20Articles/Sockets/tcpclient_py.txt
#Client Example
import socket
import time


HOME_TCP_IP = '10.0.1.3'
SCHOOL_TCP_IP = '10.2.177.254'
PHONE_TCP_IP = '10.22.218.220'
HOME_IP_PORT = 54254
SCHOOL_IP_PORT = 52790
#IP_PORTQ = raw_input("What is your IP Port? ")
#IP_Address = raw_input("What is your IP Address? ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect((SCHOOL_TCP_IP, SCHOOL_IP_PORT))
client_socket.connect((HOME_TCP_IP, HOME_IP_PORT))
#client_socket.connect((IP_Address, IP_PORTQ))
#data1 = raw_input('q' and 'Q')
data = client_socket
while 1:
    data = client_socket.recv(1000)



    if ( data == 'q' or data == 'Q'):
        split = data.split(',')
        axisY = split[6]
        client_socket.close()



        break;

    if data == "SHUTDOWN" :
        split = data.split(',')
        print "RECEIVED:", split
        client_socket.send(data)
        client_socket.close()


        break;


    else:
        split = data.split(',')
        print "RECIEVED:" , split[6]

        #time.sleep(0.8)
        #data = raw_input ( "SEND: ( TYPE q or Q to Quit):" )

        if (data <> 'Q' and data <> 'q'):
            client_socket.send(data)
        else:
            client_socket.send(data)
            client_socket.close()

            break;

        #if split[6] >= 2:
         #   client_socket.close()
          #  break;








#To Do List
#Split data -- Done
#Create an array off information -- Done
#Continuous information loop until input break -- Change to when button pressed (pause button on phone)
#Parse Comma Separated Values -- Done
#Split at [6] -- Done


#Progress
#Found ClientSocket code -- Done
#Understood how it works -- Done
#Figured out how to split data -- Done
#Still have to figure out how to -- Done
#Have to send email to PE teacher


#Ideas
#Run multiple files concurrently
#Don't need one file with everything
#Multiple files but run by one file

#When Arduino recieves input
#Stops all files together
