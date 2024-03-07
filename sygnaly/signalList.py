import signal

for sig in signal.Signals:
    print(sig.value, signal.Signals(sig).name)
# https://man7.org/linux/man-pages/man7/signal.7.html