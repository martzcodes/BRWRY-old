#########################################################################################
#
# devSerial.py
#
# This software hosts the development serial communication code for the control of the
# BRWRY automation system.  The arduino should be connected to the Raspberry Pi board by
# USB.  This creates the file serialTest.txt to collect the transmitted data.
#
# Copyright (c) 2012 Matthew A. Martz
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
#########################################################################################

import serial
from time import sleep

DEVICE = '/dev/ttyACM0'
BAUD = 9600
ser = serial.Serial(DEVICE, BAUD)

target = open("serialTest.txt", 'w')
target.truncate()

sleep(0.5)

ser.write('Hey')
sleep(0.5)
#for line in ser :
#	print line
buffer = ''
last_received = ''
buffer = buffer + ser.read(ser.inWaiting())
if '\n' in buffer:
	lines = buffer.split('\n')
	last_received = lines[-2]
	buffer = lines[-1]
	
print "Last Received:",last_received
print "Buffer:",buffer
	
line = ser.readline()
target.write(line)
print line
ser.write(raw_input("> "))
sleep(0.5)
line = ser.readline()
target.write(line)
print line
ser.write(raw_input("> "))
sleep(0.5)
line = ser.readline()
target.write(line)
print line
ser.write(raw_input("> "))
sleep(0.5)
line = ser.readline()
target.write(line)
print line
ser.write(raw_input("> "))
sleep(0.5)
line = ser.readline()
target.write(line)

target.close()