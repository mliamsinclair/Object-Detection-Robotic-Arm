import time
import serial

ser = serial.Serial('COM4', 9600)

# test serial connection
input = input("Enter 0")
if input == '0':
    print("Data sent.")
    ser.write('R')
