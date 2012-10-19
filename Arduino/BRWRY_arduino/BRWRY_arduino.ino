
/*
 * BRWRY_Arduino
 *
 * This software hosts the serial communication code, PID algorithm and direct hardware control
 * of the BRWRY automation system.  The arduino should be connected to the Raspberry Pi board
 * by USB.
 *
 * Copyright (c) 2012 Matthew A. Martz
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this
 * software and associated documentation files (the "Software"), to deal in the Software
 * without restriction, including without limitation the rights to use, copy, modify,
 * merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
 * persons to whom the Software is furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 * BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 2

int receiveCount = 0;
int stepCount = 0;
int bm = 0; //BK PID Mode
int bt = 0;//BK Target Temp
int rm = 0; //RIMS PID Mode
int rt = 0; //RIMS Target Temp
int am = 0; //BK Heating Element 1 Status
int at = 0; //BK Heating Element 2 Status
int v1 = 0; //Valve 1 Status
int v2 = 0; //Valve 2 Status
int v3 = 0; //Valve 3 Status
int v4 = 0; //Valve 4 Status
int v5 = 0; //Valve 5 Status
int v6 = 0; //Valve 6 Status
int p1 = 0; //Pump Status
int p2 = 0; //RIMS Heating Element Status
float t1 = 0.0; //Temp Sensor 1
float t2 = 0.0; //Temp Sensor 2
float t3 = 0.0; //Temp Sensor 3
float t4 = 0.0; //Temp Sensor 4
float t5 = 0.0; //Temp Sensor 5
int rpistep = 0;
int rpibm = 0; //BK PID Mode
int rpibt = 0;//BK Target Temp
int rpirm = 0; //RIMS PID Mode
int rpirt = 0; //RIMS Target Temp
int rpiam = 0; //BK Heating Element 1 Instruction
int rpiat = 0; //BK Heating Element 2 Instruction
int rpiv1 = 0; //Valve 1 Instruction
int rpiv2 = 0; //Valve 2 Instruction
int rpiv3 = 0; //Valve 3 Instruction
int rpiv4 = 0; //Valve 4 Instruction
int rpiv5 = 0; //Valve 5 Instruction
int rpiv6 = 0; //Valve 6 Instruction
int rpip1 = 0; //Pump Instruction
int rpip2 = 0; //Pump Instruction
boolean checkTemp = true;

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

DeviceAddress t1add = { 0x28, 0x7C, 0x5B, 0xCB, 0x03, 0x00, 0x00, 0x57 };

void setup () {

  Serial.begin(9600);
  establishContact();
  
  sensors.begin(); // IC Default 9 bit. If you have troubles consider upping it 12. Ups the delay giving the IC more time to process the temperature measurement
  
  sensors.setResolution(t1add, 10);
};

void loop () {
  
  if (Serial.available() == 0) {
    endLine();
  }
  
  while (Serial.available() > 0) {
    
    checkTemp = false;
    
    switch (receiveCount) {
      case 0:
      rpistep = Serial.parseInt();
      break;
      case 1:
      rpibm = Serial.parseInt(); //BK PID Mode
      break;
      case 2:
      rpibt = Serial.parseInt();//BK Target Temp
      break;
      case 3:
      rpirm = Serial.parseInt(); //RIMS PID Mode
      break;
      case 4:
      rpirt = Serial.parseInt(); //RIMS Target Temp
      break;
      case 5:
      rpiam = Serial.parseInt(); //Alt Element Mode Instruction
      break;
      case 6:
      rpiat = Serial.parseInt(); //Alt Element Target Temp Instruction
      break;
      case 7:
      rpiv1 = Serial.parseInt(); //Valve 1 Instruction
      break;
      case 8:
      rpiv2 = Serial.parseInt(); //Valve 2 Instruction
      break;
      case 9:
      rpiv3 = Serial.parseInt(); //Valve 3 Instruction
      break;
      case 10:
      rpiv4 = Serial.parseInt(); //Valve 4 Instruction
      break;
      case 11:
      rpiv5 = Serial.parseInt(); //Valve 5 Instruction
      break;
      case 12:
      rpiv6 = Serial.parseInt(); //Valve 6 Instruction
      break;
      case 13:
      rpip1 = Serial.parseInt(); //Pump Instruction
      break;
      case 14:
      rpip2 = Serial.parseInt(); //Pump Instruction
      break;
    }
    
    receiveCount = receiveCount + 1;
  }
 
  if (checkTemp) {
      sensors.requestTemperatures(); // Send the command to get temperatures
      t1 = sensors.getTempF(t1add);
  }
};

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println("Hello?");
    delay(1000);
  }
};

void sendData() {
  Serial.print("step,");
  Serial.print(stepCount); //Step
/*  Serial.print(";bkRadios,");
  Serial.print(bm);  //BK PID Mode
  Serial.print(";bktarget,");
  Serial.print(bt);  //BK Target Temp
  Serial.print(";rimsRadios,");
  Serial.print(rm); //RIMS PID Mode
  Serial.print(";rimstarget,");
  Serial.print(rt); //RIMS Target Temp
  Serial.print(";altRadios,");
  Serial.print(am); //Alt Mode
  Serial.print(";alttarget,");
  Serial.print(at); //Alt Target
  Serial.print(";v1Radios,");
  Serial.print(v1); //Valve 1
  Serial.print(";v2Radios,");
  Serial.print(v2); //Valve 2
  Serial.print(";v2Radios,");
  Serial.print(v3); //Valve 3 Status
  Serial.print(";v2Radios,");
  Serial.print(v4); //Valve 4 Status
  Serial.print(";v2Radios,");
  Serial.print(v5); //Valve 5 Status
  Serial.print(";v2Radios,");
  Serial.print(v6); //Valve 6 Status
  Serial.print(";p1Radios,");
  Serial.print(p1); //Pump 1 Status
  Serial.print(";p2Radios,");
  Serial.print(p2); //Pump 2 Status
  */
  Serial.print(";temp_bk,");
  Serial.print(t1); //Temp Sensor 1
  Serial.print(";temp_rims,");
  Serial.print(t2); //Temp Sensor 2
  Serial.print(";temp_alt1,");
  Serial.println(t3); //Temp Sensor 3
  Serial.print(";temp_alt2,");
  Serial.println(t4); //Temp Sensor 4
  Serial.print(";temp_alt3,");
  Serial.println(t5); //Temp Sensor 5
}

void endLine() {
  if (receiveCount == 15) {
    checkData();
  }
  if (receiveCount > 0) {
//    Serial.println(receiveCount);
    sendData();
  }
  checkTemp = true;
  resetData();
  receiveCount = 0;
};

void checkData() {
  //Make sure the data looks right
  
  //For now just pass it along
  updateData();
};

void updateData() {
  //Update the current values
  stepCount = rpistep;
  bm = rpibm;
  bt = rpibt;
  rm = rpirm;
  rt = rpirt;
  am = rpiam;
  at = rpiat;
  v1 = rpiv1;
  v2 = rpiv2;
  v3 = rpiv3;
  v4 = rpiv4;
  v5 = rpiv5;
  v6 = rpiv6;
  p1 = rpip1;
  p2 = rpip2;
};

void resetData() {
  //Reset the input data
  rpistep = 0;
  rpibm = 0; //BK PID Mode
  rpibt = 0;//BK Target Temp
  rpirm = 0; //RIMS PID Mode
  rpirt = 0; //RIMS Target Temp
  rpiam = 0; //BK Heating Element 1 Instruction
  rpiat = 0; //BK Heating Element 2 Instruction
  rpiv1 = 0; //Valve 1 Instruction
  rpiv2 = 0; //Valve 2 Instruction
  rpiv3 = 0; //Valve 3 Instruction
  rpiv4 = 0; //Valve 4 Instruction
  rpiv5 = 0; //Valve 5 Instruction
  rpiv6 = 0; //Valve 6 Instruction
  rpip1 = 0; //Pump Instruction
  rpip2 = 0; //Pump Instruction
};
