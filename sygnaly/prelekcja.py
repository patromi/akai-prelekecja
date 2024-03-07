import signal
import time
import threading
import datetime




signal_status = 0
def handler(sig, frame):
    print("Wykryto sygnał",sig)
    global signal_status
    signal_status = sig
    #exit()
for sig in signal.Signals:
    if sig ==9 or sig == 19: continue
    signal.signal(sig, handler)



def processing():
    print(datetime.datetime.now(), "Początek wątku ", threading.current_thread())
    time.sleep(5)
    print(datetime.datetime.now(), "Początek koniec ", threading.current_thread())

while True:
    t = threading.Thread(target=processing)
    t.start()
    time.sleep(1)
    if signal_status:
        print("Program zakończył się pomyślnie")
        exit()