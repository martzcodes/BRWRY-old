
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
#include <string.h>

// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 2
// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);
DeviceAddress t1add = { 0x28, 0x7C, 0x5B, 0xCB, 0x03, 0x00, 0x00, 0x57 };

boolean dataReceived = false;
int semiCount = 0;
int semiLoc[20];
String inMsg = "";
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

void setup() {
  Serial.begin(9600);
  sensors.begin();
  sensors.setResolution(t1add,10);
  memset(semiLoc,0,sizeof(semiLoc));
}

void loop() {
   if (Serial.available() == 0 && dataReceived) {
//     Serial.println("Message: " + inMsg);
     
//     Serial.println("Message part: " + inMsg.substring(10,20));
     
     int x = 0;
     semiCount = 0;
     memset(semiLoc,0,sizeof(semiLoc));
     while(x<inMsg.length()){
       x = inMsg.indexOf(';',x+1);
       if (x != -1) {
         semiLoc[semiCount] = x;
//         Serial.print("semicolon at: ");
//         Serial.println(x);
         semiCount++;
       } else {
         semiLoc[semiCount] = inMsg.indexOf('\n');
//         Serial.println("newline at: " + String(semiLoc[semiCount]));
         semiCount++;
       }
     }
     int instType = inMsg.substring(0,semiLoc[0]).toInt();
//     Serial.println("In between: " + printmsg);
     String printmsg = "";     
     for (int y=1; y<=semiCount-1; y++) {
       printmsg = inMsg.substring(semiLoc[y-1]+1,semiLoc[y]);
       if (printmsg != "") {
//         Serial.println("In between: " + printmsg);
         processIncoming(printmsg,instType);
       }
     }
//     Serial.println("There are " + String(semiCount) + " semicolons.");
//     Serial.println("inMsg length is: " + String(inMsg.length()));
     if (instType > stepCount) {
       stepCount = instType;
     }
     inMsg = "";
     dataReceived = false;
     sendData();
   }
   
   while (Serial.available() > 0) {
     delay(3);
     char inChar = Serial.read();
     inMsg += inChar;
     dataReceived = true;
     
   }
}

void processIncoming (String procMsg, int instType) {
  int commaIndex = procMsg.indexOf(',');
  if (commaIndex == -1) {
    // Serial.println("No commas");
  } else {
    if (procMsg.indexOf(',',commaIndex+1) == -1) {
      // Serial.println("There are commas");
      String incAdd = procMsg.substring(0,commaIndex);
      String incInst = procMsg.substring(commaIndex+1,procMsg.length());
//      Serial.println("Instruction address: " + incAdd + " | " + incInst);
      if (instType > stepCount) {
        updateInstruction(incAdd,incInst);
      } else {
        updateHardware(incAdd,incInst);
      }
    } else {
      //too many commas
    }
  }
}

void updateInstruction(String incAdd, String incInst) {    
  if (incAdd == "BM") {
    bm = incInst.toInt();
  }
  if (incAdd == "BT") {
    bt = incInst.toInt();
  }
  if (incAdd == "RM") {
    rm = incInst.toInt();
  }
  if (incAdd == "RT") {
    rt = incInst.toInt();
  }
  if (incAdd == "AM") {
    am = incInst.toInt();
  }
  if (incAdd == "AT") {
    at = incInst.toInt();
  }
  if (incAdd == "V1") {
    v1 = incInst.toInt();
  }
  if (incAdd == "V2") {
    v2 = incInst.toInt();
  }
  if (incAdd == "V3") {
    v3 = incInst.toInt();
  }
  if (incAdd == "V4") {
    v4 = incInst.toInt();
  }
  if (incAdd == "V5") {
    v5 = incInst.toInt();
  }
  if (incAdd == "V6") {
    v6 = incInst.toInt();
  }
  if (incAdd == "P1") {
    p1 = incInst.toInt();
  }
  if (incAdd == "P2") {
    p2 = incInst.toInt();
  }
}

void updateHardware(String incAdd, String incInst) {
  if (incAdd == "T1") {
    //
  }
  if (incAdd == "T2") {
    //
  }
  if (incAdd == "T3") {
    //
  }
  if (incAdd == "T4") {
    //
  }
  if (incAdd == "T5") {
    //
  }
  if (incAdd == "H1") {
    //
  }
  if (incAdd == "H2") {
    //
  }
  if (incAdd == "H3") {
    //
  }
  if (incAdd == "V1") {
    //
  }
  if (incAdd == "V2") {
    //
  }
  if (incAdd == "V3") {
    //
  }
  if (incAdd == "V4") {
    //
  }
  if (incAdd == "V5") {
    //
  }
  if (incAdd == "V6") {
    //
  }
  if (incAdd == "P1") {
    //
  }
  if (incAdd == "P2") {
    //
  }
}

void sendData() {
  checkTemp();
  Serial.print("step,");
  Serial.print(stepCount); //Step
  /*
  Serial.print(";bkRadios,");
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
  Serial.print(";v3Radios,");
  Serial.print(v3); //Valve 3 Status
  Serial.print(";v4Radios,");
  Serial.print(v4); //Valve 4 Status
  Serial.print(";v5Radios,");
  Serial.print(v5); //Valve 5 Status
  Serial.print(";v6Radios,");
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

void checkTemp () {
  sensors.requestTemperatures(); // Send the command to get temperatures
  t1 = sensors.getTempF(t1add);
}
