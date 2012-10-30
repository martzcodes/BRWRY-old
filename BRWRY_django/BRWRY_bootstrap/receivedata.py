import serial, time, json, os.path

t_b = [0.0,0.0,0.0,0.0]
t_r = [0.0,0.0,0.0,0.0]
t_a1 = [0.0,0.0,0.0,0.0]
t_a2 = [0.0,0.0,0.0,0.0]
t_a3 = [0.0,0.0,0.0,0.0]
temp = 0
jsonlinesallowed = 1000

def jsonoutput(lasttime):
	t_b_out = (t_b[0]+t_b[1]+t_b[2]+t_b[3])/4.0
	t_r_out = (t_r[0]+t_r[1]+t_r[2]+t_r[3])/4.0
	t_a1_out = (t_a1[0]+t_a1[1]+t_a1[2]+t_a1[3])/4.0
	t_a2_out = (t_a2[0]+t_a2[1]+t_a2[2]+t_a2[3])/4.0
	t_a3_out = (t_a3[0]+t_a3[1]+t_a3[2]+t_a3[3])/4.0

	brwnametarget = open("static/data/brwName.txt")
	brwname = brwnametarget.read()
	brwnametarget.close()
	
	jsonfilename = "static/data/"+brwname+".json"
	if (os.path.isfile(jsonfilename)):
		jsontarget = open(jsonfilename)
		jsonexist = jsontarget.read()
		jsontarget.close()
	else:
		jsonexist = ''

	t_blines = 0;
	if len(jsonexist) > 0:
		jsondata = json.loads(jsonexist)
		t_blines = len(jsondata[u't_b'][u'data'])
	else:
		jsondata = {u't_b':{u'label':u'Boil Kettle Temp',u'data':[]},
					u't_r':{u'label':u'RIMS Temp',u'data':[]},
					u't_a1':{u'label':u'Alt 1 Temp',u'data':[]},
					u't_a2':{u'label':u'Alt 2 Temp',u'data':[]},
					u't_a3':{u'label':u'Alt 3 Temp',u'data':[]},}
		t_blines = 0
	while t_blines >= jsonlinesallowed:
		jsondata[u't_b'][u'data'].pop(0)
		jsondata[u't_r'][u'data'].pop(0)
		jsondata[u't_a1'][u'data'].pop(0)
		jsondata[u't_a2'][u'data'].pop(0)
		jsondata[u't_a3'][u'data'].pop(0)
		t_blines -= 1
	jsondata[u't_b'][u'data'].append([lasttime, float(t_b_out)])
	jsondata[u't_r'][u'data'].append([lasttime, float(t_r_out)])
	jsondata[u't_a1'][u'data'].append([lasttime, float(t_a1_out)])
	jsondata[u't_a2'][u'data'].append([lasttime, float(t_a2_out)])
	jsondata[u't_a3'][u'data'].append([lasttime, float(t_a3_out)])
	jsontarget = open(jsonfilename,"w")
	jsontarget.truncate()
	jsondump = json.dumps(jsondata)
	jsontarget.write(jsondump)
	jsontarget.close()

ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(4)
ser.write('0')
time.sleep(1)

while ser.inWaiting() >0:
    ser.read()  #flush the old data to make room for new

while 1:
	ser.write('0')
	time.sleep(0.5)
	if ser.inWaiting() > 0:
		line = ser.readline()
		
		linesplit = line.split(';')
		linedict = dict((k.strip(), v.strip()) for k,v in 
						(item.split(',') for item in linesplit))
		linedict["time"] = int(time.time()) #update time
		
		target = open("static/data/liveData.dat", 'w')
		target.truncate()
		
		lineout = str(linedict["time"]) + ","
		lineout += str(linedict["temp_bk"])+","+str(linedict["temp_rims"])
		lineout += ","+str(linedict["temp_alt1"])+","
		lineout += str(linedict["temp_alt2"])+","+str(linedict["temp_alt3"])
		
		target.write(lineout)
		target.close()
		time.sleep(0.5)
		
		t_b[temp] = float(linedict["temp_bk"])
		t_r[temp] = float(linedict["temp_rims"])		
		t_a1[temp] = float(linedict["temp_alt1"])
		t_a2[temp] = float(linedict["temp_alt2"])
		t_a3[temp] = float(linedict["temp_alt3"])
		
		if temp == 3:
			#write arrays to json file
			if (os.path.isfile("static/data/brwName.txt")):
				jsonoutput(int(linedict['time']))
			temp = 0
		else:
			temp += 1