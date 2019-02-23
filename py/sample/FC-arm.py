from pymultiwii import MultiWii
import time

if __name__ == "__main__":

    #board = MultiWii("/dev/tty.usbserial-AM016WP4")
    #board = MultiWii("/dev/serial0") 
    board = MultiWii("/dev/ttyUSB0")
    try:
        board.arm()
        print ("Board is armed now!")
        print ("In 3 seconds it will disarm...")
        time.sleep(3)
        board.disarm()
        print ("Disarmed.")
        time.sleep(3)

    except Exception,error:
        print ("Error on Main: "+str(error))