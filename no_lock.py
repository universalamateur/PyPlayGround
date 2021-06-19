## This script will simulate a keypress and prevent Windows from locking

import time

def no_lock(button):
    try:
        print ('Press CTRL+C to stop.')
        while True:
            time.sleep(2)
            time.sleep(3)

    except Exception as ex:
        print ('no_lock | Error: ', ex)

def main():
    try:
        print ('\nPrevent Windows screenlock')
        kb_button = str(input('Enter keyboard button: '))
        
        print ('\nRunning')
        no_lock(kb_button)

    except KeyboardInterrupt:
        print('\nStopped')

    except Exception as ex:
        print ('main | Error: ', ex)

if __name__ == "__main__":
    main()