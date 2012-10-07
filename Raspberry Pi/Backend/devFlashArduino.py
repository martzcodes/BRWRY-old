#########################################################################################
#
# devFlashArduino.py
#
# This software hosts the development code to flash the Arduino with a hex file.
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

import subprocess as sub
import serial
from time import sleep

#boardType = 'Arduino Uno'
hexFile = 'BRWRY_arduino.cpp.hex'
port = '/dev/ttyACM0'
avrconf = '/usr/share/arduino/hardware/tools/avrdude.conf'
#boardsFile = open('/usr/share/arduino/hardware/arduino/boards.txt','rb').readlines()
#boardSettings = {}
#returnString = ""

#avrsizeCommand = 'avr-size ' + hexFile
# check program size against maximum size
#p = sub.Popen(avrsizeCommand, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
#output, errors = p.communicate()
#if errors != "":
#    returnString = returnString + 'avr-size error: ' + errors + '\n'
#    print returnString

#returnString = returnString + ('Progam size: ' + output.split()[7] +
#    ' bytes out of max 32256 \n')

programCommand = ('avrdude' +
            ' -F ' +
            ' -p atmega328p' +
            ' -c arduino' + 
            ' -b 115200' + 
            ' -P ' + port +
            ' -U ' + 'flash:w:' + hexFile +
            ' -C ' + avrconf)

p = sub.Popen(programCommand, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
output, errors = p.communicate()
# avrdude only uses stderr, append it
#returnString = returnString + errors
print errors