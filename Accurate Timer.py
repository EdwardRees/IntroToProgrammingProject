import time 
  
Sec=0
Min=0
Lap=0

time1=time.time()
time2=time.time()

while True:

  time.sleep(1)
  time2=time.time()
  print(time2-time1)
  Sec += 1
  secClock = (str(Min) + " Mins " + str(Sec) + " Sec ")
  print secClock
  if Sec == 60:
    Sec = 0
    Min += 1
    clock = (str(Min) + " Minute")
    print(clock)
