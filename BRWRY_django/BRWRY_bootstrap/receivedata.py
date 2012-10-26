import serial, time, json

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

	jsontarget = open("static/data/testdata.json")
	jsonexist = jsontarget.read()
	jsontarget.close()

	jsonlines = 0
	if len(jsonexist) > 0:
		jsondata = json.loads(jsonexist)
		jsonlines = len(jsondata[u'data'])
	else:
		jsondata = {u'label':u'Boil Kettle Temp',u'data':[]}
	while jsonlines >= jsonlinesallowed:
		jsondata[u'data'].pop(0)
		jsonlines -= 1
	jsondata[u'data'].append([lasttime, float(t_b_out)])
	jsontarget = open("static/data/testdata.json","w")
	jsontarget.truncate()
	jsondump = json.dumps(jsondata)
	jsontarget.write(jsondump)
	jsontarget.close()

ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
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
			jsonoutput(int(linedict['time']))
			temp = 0

		temp += 1