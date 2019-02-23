from pymultiwii import MultiWii
from sys import stdout
import time
if __name__ == "__main__":
    #board = MultiWii("/dev/ttyUSB0")
    board = MultiWii("/dev/serial0") 
    try:
        print ("start")
        board.arm()
        print ("armed")
        while True:        
            data = [1500,1550,1600,1560,1000,1040,1000,1000]
            board.sendCMDreceiveATT(16,MultiWii.SET_RAW_RC,data)
            #board.sendCMD(16,MultiWii.SET_RAW_RC,data)
            print board.getData(MultiWii.RC)
            time.sleep(0.5)
    except Exception,error:
        print "Error on Main: "+str(error)
        print("end")
