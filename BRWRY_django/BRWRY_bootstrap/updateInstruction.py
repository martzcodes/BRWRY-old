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

import os
import time
import simplejson as json

def updateInstruction(insts):

    archInst = open("insts.txt")
    archInstlist = archInst.readlines()
    lastLine = archInstlist[-1].split(';')
    if lastLine[0] == '\n':
        instNum = 1
    else:
        instNum = int(lastLine[0])+1
    archInst.close()
    
    lastLine.pop(0)
    lastLine.pop(-1)
    
    instdict = dict((k.strip(), v.strip()) for k,v in 
                    (item.split(',') for item in lastLine))
    
    archseg=''
    archseg+=str(instNum)+';'
#    target.write(instNum)
#    target.write(';bm,')
    if insts['bkRadios'] == 'ON':
        archseg+='bm,1;'
    elif insts['bkRadios'] == 'PID':
        archseg+='bm,2;'
    else:
        archseg+='bm,0;'
#    target.write(seg)
#    target.write('bt,')
#    target.write(insts['bktarget'])
#    target.write(';')
    archseg+='bt,'+str(insts['bktarget'])+';'
    archseg+='rm,'
    if insts['rimsRadios'] == 'ON':
        archseg+='1;rt,'
    elif insts['rimsRadios'] == 'PID':
        archseg+='2;rt,'
    else:
        archseg+='0;rt,'
#    target.write(seg)
#    target.write(insts['rimstarget'])
#    target.write(';')
    archseg+=str(insts['bktarget'])
    archseg+=';am,'
    if insts['altRadios'] == 'ON':
        archseg+='1;at,'
    elif insts['altRadios'] == 'PID':
        archseg+='2;at,'
    else:
        archseg+='0;at,'
#    target.write(seg)
#    target.write(insts['alttarget'])
#    target.write(';')
    archseg+=str(insts['alttarget'])
    archseg+=';V1,'
    if insts['v1Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
    archseg+='V2,'
    if insts['v2Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
    archseg+='V3,'
    if insts['v3Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
    archseg+='V4,'
    if insts['v4Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
    archseg+='V5,'
    if insts['v5Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
    archseg+='V6,'
    if insts['v6Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
    archseg+='P1,'
    if insts['p1Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
    archseg+='P2,'
    if insts['p2Radios'] == 'ON':
        archseg+='1;'
    else:
        archseg+='0;'
#    target.write(seg)
        
#    target.write('\n')
    
#    print archseg
    
    instseg = ''
    
    tempseg = archseg.split(';')
    tempseg.pop(0)
    tempseg.pop(-1)
    
    archdict = dict((k.strip(), v.strip()) for k,v in 
                    (item.split(',') for item in tempseg))
                    
    for key in instdict:
        if instdict[key] != archdict[key]:
            instseg+=key+','+archdict[key]+';'
        
    if instseg != '':
        instseg+='\n'
        tempseg = instseg
        instseg = str(instNum)+';'
        instseg += tempseg
        target = open("instruction.txt",'w')
        target.truncate()
        target.write(instseg)
        target.close()
        print instseg

        archseg+='\n'
        archInst = open("insts.txt","a")
        archInst.write(archseg)
        archInst.close()
    else:
        print "no changes, nothing written"
    
    print os.stat('instruction.txt').st_mtime

    print "Update done!"