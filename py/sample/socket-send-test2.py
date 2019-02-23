import socket
import pygame
from pygame.locals import *
import time

IP = '192.168.100.111'
PORT = 50000
BUFFER_SIZE = 2048
    
def INPUT():
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print ('joystick start')

    pygame.init()

    while True:
         # コントローラーの操作を取得
        eventlist = pygame.event.get()

        # イベント処理
        for e in eventlist:
            if e.type == QUIT:
                return 'XXX'

            if e.type == pygame.locals.JOYAXISMOTION:
                x, y = joystick0.get_axis(0), joystick0.get_axis(1)
                print ('axis x:' + str(x) + ' axis y:' + str(y))
            elif e.type == pygame.locals.JOYHATMOTION:
                x, y = joystick0.get_hat(0)
                print ('hat x:' + str(x) + ' hat y:' + str(y))
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                print ('button:' + str(e.button))
                data = str(e.button)
                return data
        time.sleep(0.1)

if __name__ == '__main__':
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((IP, PORT))
                Sdata = INPUT()
                s.send(Sdata.encode())
                Rdata = s.recv(BUFFER_SIZE)
                print(Rdata.decode())
        except pygame.error:
            print ('joystickが見つかりませんでした。')
        except KeyboardInterrupt:
            connection.close()
            print('Done')