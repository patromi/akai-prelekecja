import datetime
import signal
import threading
import time


def processing():
    print(datetime.datetime.now(), "Początek wątku ", threading.current_thread())
    time.sleep(5)
    print(datetime.datetime.now(), "Początek koniec ", threading.current_thread())
