import sys
import serial
import time
import csv

ser = serial.Serial('/dev/ttyUSB0')
old_reading = 0
while True:
    moisture_reading = ser.readline()
    if moisture_reading != old_reading:
        row = [time.ctime(), time.time(), int(moisture_reading)]
        with open('moisturelog.csv', 'a') as moisture_log:
            w = csv.writer(moisture_log)
            w.writerow(row)

    old_reading = moisture_reading
