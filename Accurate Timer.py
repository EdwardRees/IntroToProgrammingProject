import time
import sys, select

text_file=open("TextFile.txt", "a")

Sec=0
Min=0
Lap=0

Start=time.time()
End=time.time()

while True:

  time.sleep(1)
  End=time.time()
  print(End-Start)
  Sec += 1
  secClock = (str(Min) + " Mins " + str(Sec) + " Sec ")
  print secClock
  
  if Sec == 60:
    Sec = 0
    Min += 1
    clock = (str(Min) + " Minute")
    print(clock)
  
  if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
    print ("finish")
    #export student time result to a textfile
    text_file.write ("Time:" + str(round(end-start, 3)) + "second(s)" + "\n" )
    break;

  
