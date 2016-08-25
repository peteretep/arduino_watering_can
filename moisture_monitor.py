import sys
import serial
import time
import csv

ser = serial.Serial('/dev/ttyUSB0')
while True:
    moistureReading = ser.readline()
    row = [time.ctime(), time.time(), int(moistureReading)]
    with open('moisturelog.csv', 'a') as moisturelog:
        w = csv.writer(moisturelog)
        w.writerow(row)
