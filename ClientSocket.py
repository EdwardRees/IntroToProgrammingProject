#http://www.pythonprasanna.com/Papers%20and%20Articles/Sockets/tcpclient_py.txt
#Client Example
import socket
import time

TCP_IP = '10.x.x.x'
TCP_PORT = xxxxx

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

data = client_socket
while 1:
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
            



