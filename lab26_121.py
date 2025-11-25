

import serial
import time

arduino_port = 'COM3'
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port,baud_rate,timeout = 1)
    time.sleep(2)
    print("LED control started.Press Ctrl+C to stop. ")
      while True:
      ser.write(b'ON\n')
      print("LED is ON")
      time.sleep(1)
      
      ser.write(b'OFF\n')
      print("LED is OFF")
      time.sleep(1)
      
except serial.SerialException as e:
    print(f"Serial error : {e}")
except KeyboardInterrupt:
    print("\nLED control stopped.")
    ser.close()
Ardunio Code (LED_Control.ino):
const int ledPin = 13;
void setup()
{
 pinMode(ledPin,OUTPUT);
 Serial.begin(9600);
}      
        