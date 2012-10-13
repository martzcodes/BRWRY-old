# import serial

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