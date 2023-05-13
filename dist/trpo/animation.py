import time
import sys

def loading_animation(duration):
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for i in range(4):
            sys.stdout.write('\r' + 'Loading' + '.' * i)
            sys.stdout.flush()
            time.sleep(0.25)
    sys.stdout.write('\r' + ' ' * 20 + '\r')

loading_animation(2)