
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

int receiveCount = 0;
int stepCount = 0;
int bm = 0; //BK PID Mode
int bt = 0;//BK Target Temp
int rm = 0; //RIMS PID Mode
int rt = 0; //RIMS Target Temp
int b1 = 0; //BK Heating Element 1 Status
int b2 = 0; //BK Heating Element 2 Status
int he = 0; //RIMS Heating Element Status
int p1 = 0; //Pump Status
int v1 = 0; //Valve 1 Status
int v2 = 0; //Valve 2 Status
int v3 = 0; //Valve 3 Status
int v4 = 0; //Valve 4 Status
int v5 = 0; //Valve 5 Status
int v6 = 0; //Valve 6 Status
int t1 = 0; //Temp Sensor 1
int t2 = 0; //Temp Sensor 2
int t3 = 0; //Temp Sensor 3
int rpibm = 0; //BK PID Mode
int rpibt = 0;//BK Target Temp
int rpirm = 0; //RIMS PID Mode
int rpirt = 0; //RIMS Target Temp
int rpib1 = 0; //BK Heating Element 1 Instruction
int rpib2 = 0; //BK Heating Element 2 Instruction
int rpihe = 0; //RIMS Heating Element Instruction
int rpip1 = 0; //Pump Instruction
int rpiv1 = 0; //Valve 1 Instruction
int rpiv2 = 0; //Valve 2 Instruction
int rpiv3 = 0; //Valve 3 Instruction
int rpiv4 = 0; //Valve 4 Instruction
int rpiv5 = 0; //Valve 5 Instruction
int rpiv6 = 0; //Valve 6 Instruction

void setup () {

  Serial.begin(9600);
  establishContact();

};

void loop () {
  
  if (Serial.available() == 0) {
    endLine();
  }
  
  while (Serial.available() > 0) {
    
    switch (receiveCount) {
      case 0:
      rpibm = Serial.parseInt(); //BK PID Mode
      break;
      case 1:
      rpibt = Serial.parseInt();//BK Target Temp
      break;
      case 2:
      rpirm = Serial.parseInt(); //RIMS PID Mode
      break;
      case 3:
      rpirt = Serial.parseInt(); //RIMS Target Temp
      break;
      case 4:
      rpib1 = Serial.parseInt(); //BK Heating Element 1 Instruction
      break;
      case 5:
      rpib2 = Serial.parseInt(); //BK Heating Element 2 Instruction
      break;
      case 6:
      rpihe = Serial.parseInt(); //RIMS Heating Element Instruction
      break;
      case 7:
      rpip1 = Serial.parseInt(); //Pump Instruction
      break;
      case 8:
      rpiv1 = Serial.parseInt(); //Valve 1 Instruction
      break;
      case 9:
      rpiv2 = Serial.parseInt(); //Valve 2 Instruction
      break;
      case 10:
      rpiv3 = Serial.parseInt(); //Valve 3 Instruction
      break;
      case 11:
      rpiv4 = Serial.parseInt(); //Valve 4 Instruction
      break;
      case 12:
      rpiv5 = Serial.parseInt(); //Valve 5 Instruction
      break;
      case 13:
      rpiv6 = Serial.parseInt(); //Valve 6 Instruction
      break;
    }
    
    receiveCount = receiveCount + 1;
  }
};

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println("Hello?");
    delay(300);
  }
};

void sendData() {
  Serial.print(stepCount); //Step
  Serial.print(",");
  Serial.print(bm);  //BK PID Mode
  Serial.print(",");
  Serial.print(bt);  //BK Target Temp
  Serial.print(",");
  Serial.print(rm); //RIMS PID Mode
  Serial.print(",");
  Serial.print(rt); //RIMS Target Temp
  Serial.print(",");
  Serial.print(b1); //BK Heating Element 1 Status
  Serial.print(",");
  Serial.print(b2); //BK Heating Element 2 Status
  Serial.print(",");
  Serial.print(he); //RIMS Heating Element Status
  Serial.print(",");
  Serial.print(p1); //Pump Status
  Serial.print(",");
  Serial.print(v1); //Valve 1 Status
  Serial.print(",");
  Serial.print(v2); //Valve 2 Status
  Serial.print(",");
  Serial.print(v3); //Valve 3 Status
  Serial.print(",");
  Serial.print(v4); //Valve 4 Status
  Serial.print(",");
  Serial.print(v5); //Valve 5 Status
  Serial.print(",");
  Serial.print(v6); //Valve 6 Status
  Serial.print(",");
  Serial.print(t1); //Temp Sensor 1
  Serial.print(",");
  Serial.print(t2); //Temp Sensor 2
  Serial.print(",");
  Serial.println(t3); //Temp Sensor 3
}

void endLine() {
  if (receiveCount == 14) {
    checkData();
  }
  if (receiveCount > 0) {
//    Serial.println(receiveCount);
    sendData();
  }
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
  stepCount = stepCount + 1;
  bm = rpibm;
  bt = rpibt;
  rm = rpirm;
  rt = rpirt;
  b1 = rpib1;
  b2 = rpib2;
  he = rpihe;
  p1 = rpip1;
  v1 = rpiv1;
  v2 = rpiv2;
  v3 = rpiv3;
  v4 = rpiv4;
  v5 = rpiv5;
  v6 = rpiv6;
};

void resetData() {
  //Reset the input data
  rpibm = 0; //BK PID Mode
  rpibt = 0;//BK Target Temp
  rpirm = 0; //RIMS PID Mode
  rpirt = 0; //RIMS Target Temp
  rpib1 = 0; //BK Heating Element 1 Instruction
  rpib2 = 0; //BK Heating Element 2 Instruction
  rpihe = 0; //RIMS Heating Element Instruction
  rpip1 = 0; //Pump Instruction
  rpiv1 = 0; //Valve 1 Instruction
  rpiv2 = 0; //Valve 2 Instruction
  rpiv3 = 0; //Valve 3 Instruction
  rpiv4 = 0; //Valve 4 Instruction
  rpiv5 = 0; //Valve 5 Instruction
  rpiv6 = 0; //Valve 6 Instruction
};
