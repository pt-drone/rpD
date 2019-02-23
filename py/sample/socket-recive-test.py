import socket
import RPi.GPIO as GPIO
import time

HOST = '192.168.100.111'
PORT = 50000
BUFFER_SIZE = 1024

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(26,GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
s.bind((HOST, PORT))
s.listen(1)

while True:
    (connection, client) = s.accept()
    try:
        print('Client connected', client)
        data = connection.recv(BUFFER_SIZE)
        if data == 'a':
            for x in xrange(5):
                GPIO.output(26,True)
                time.sleep(0.5)
                GPIO.output(26,False)
                time.sleep(0.5)
            connection.send('ok')
            print ('Pika')
        else:
            break
    except KeyboardInterrupt:
        connection.close()
        GPIO.cleanup()
        print('Done')

connection.close()
GPIO.cleanup()
print('Done')
