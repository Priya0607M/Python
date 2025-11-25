# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 17:01:33 2025

@author: Priya
"""

import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

while True:
    message = input("Type a message to send to arduino : ")
    
    arduino.write(message.encode())
    
    print("Message sent!\n")