#!/usr/bin/env python

import serial
import sys
import time
from time import strftime
from sys import platform
from re import search

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
    log = ser.readline()
    log = log.decode("utf-8")
    match = search('^[0-9]{,2}.[0-9]{,2}', log)

    # só salva os dados quando a saída do arduino
    # for válida.
    if match:
        log = match.group(0)
    else:
        continue

    time = strftime("%H:%M:%S")
    hour = time[0:2]
    minute = time[3:5]
    second = time[6:]

    text = time + " - " + log + "\n"

    # a cada 10 minutos salva a temperatura
    if hits == 600:

        hits = 0
        ten_mins += 1

        f = open("temp_10min.txt", "a")
        f.write(text)
        f.close()

        # a cada 1 hora salva a temperatura
        # em outro arquivo
        if ten_mins == 6:

            ten_mins = 0

            f = open("temp_1hour.txt", "a")
            f.write(text)
            f.close()

    print(f"{text}", end="")
    hits += 1
