from pymultiwii import MultiWii
from sys import stdout
import time
if __name__ == "__main__":
	#board = MultiWii("/dev/ttyUSB0")
	board = MultiWii("/dev/serial0") 
	try:
		while True:
			board.getData(MultiWii.ATTITUDE)
			print board.attitude
			time.sleep(1)
	except Exception,error:
		print "Error on Main: "+str(error)
