import time

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
