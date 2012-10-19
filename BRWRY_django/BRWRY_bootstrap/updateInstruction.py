#########################################################################################
#
# updateInstruction.py
#
# This file updates the instruction file from the control panel of the BRWRY automation
# system.  The arduino should be connected to the Raspberry Pi board by USB.
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


def updateInstruction(insts):
    target = open("instruction.txt",'w')
    target.truncate()
    seg=''
    if insts['bkRadios'] == 'ON':
        seg='1,'
    elif insts['bkRadios'] == 'PID':
        seg='2,'
    else:
        seg='0,'
    target.write(seg)
    target.write(insts['bktarget'])
    target.write(',')
    if insts['rimsRadios'] == 'ON':
        seg='1,'
    elif insts['rimsRadios'] == 'PID':
        seg='2,'
    else:
        seg='0,'
    target.write(seg)
    target.write(insts['rimstarget'])
    target.write(',')
    if insts['altRadios'] == 'ON':
        seg='1,'
    elif insts['altRadios'] == 'PID':
        seg='2,'
    else:
        seg='0,'
    target.write(seg)
    target.write(insts['alttarget'])
    target.write(',')
    if insts['v1Radios'] == 'ON':
        seg='1,'
    else:
        seg='0,'
    target.write(seg)
    if insts['v2Radios'] == 'ON':
        seg='1,'
    else:
        seg='0,'
    target.write(seg)
    if insts['v3Radios'] == 'ON':
        seg='1,'
    else:
        seg='0,'
    target.write(seg)
    if insts['v4Radios'] == 'ON':
        seg='1,'
    else:
        seg='0,'
    target.write(seg)
    if insts['v5Radios'] == 'ON':
        seg='1,'
    else:
        seg='0,'
    target.write(seg)
    if insts['v6Radios'] == 'ON':
        seg='1,'
    else:
        seg='0,'
    target.write(seg)
    if insts['p1Radios'] == 'ON':
        seg='1,'
    else:
        seg='0,'
    target.write(seg)
    if insts['p2Radios'] == 'ON':
        seg='1'
    else:
        seg='0'
    target.write(seg)
        
    target.write('\n')
    target.close()
    print "Update done!"