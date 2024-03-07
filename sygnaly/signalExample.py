import signal
from datetime import datetime
import time
import threading

signal_status = 0


def handler(signum, frame):
    print('Signal handler called with signal', signum)
    global signal_status
    signal_status = signum
    exit()


def proccssing():
    print(datetime.now(), 'Processing transaction', signal_status)
    time.sleep(10)
    print(datetime.now(), 'Finish transaction', signal_status, threading.current_thread().name)


for sig in signal.Signals:
    print(sig.value, signal.Signals(sig).name)
    if sig == 9 or sig == 19: continue
    signal.signal(sig, handler)

while True:
    print(datetime.now(), 'Waiting for signal...')
    t = threading.Thread(target=proccssing)
    t.start()
    time.sleep(1)
    print(threading.active_count())
    if signal_status and threading.active_count() == 0:
        print('Signal received successfully, exiting...')
        exit()
