import time
Sec = 0
Min = 0
Lap = 0
while True:
        Sec += 1
        print (str(Min) + " Mins " + str(Sec) + " Sec ")
        time.sleep(1)
        if Sec == 60:
            Sec = 0
            Min += 1
            print(str(Min) + " Minute")
