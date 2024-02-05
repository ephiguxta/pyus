import serial
import sys
import time
from time import strftime
from sys import platform

baudrate = '9600'

port = ''
if platform == 'linux':
    port = '/dev/ttyUSB0'
else:
    port = 'COM3'

# TODO: possibilidade de passar por parâmetros
ser = serial.Serial(port, baudrate)

hits = 0
ten_mins = 0

while(True):
    log = str(ser.readline())

    time = strftime("%H:%M:%S")
    hour = time[0:2]
    minute = time[3:5]
    second = time[6:]

    text = time + " - " + log[2:7] + "\n"

    # salvando a temperatura a cada 10 minutos,
    # há 600 segundos em 10min.
    if hits == 600 and ten_mins != 6:

        hits = 0
        ten_mins += 1

        f = open("temp_10min.txt", "a")
        f.write(text)
        f.close()

    # 60 minutos == 1 hora
    elif ten_mins == 6:
        ten_mins = 0

        f = open("temp_1hour.txt", "a")
        f.write(text)
        f.close()

    else:
        f = open("temp_secs.txt", "a")
        f.write(text)
        f.close()

    print(text, end="")
    hits += 1
