import time

while True:
    try:
        input('Press Enter to continue, CTRL+c to Exit.')
        startTime = time.time()
        while True:
            print('Time elapsed =', round(time.time() - startTime), 'secs', end='\n')
            time.sleep(1)

    except KeyboardInterrupt: # CTRL + c
        print('Time has stopped')
        endTime = time.time()
        print('The time elapsed is', round(endTime - startTime, 2), 'secs')
        break