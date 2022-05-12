# Motion_Detector_RPi
Motion sensor using PIR module in RPi4
This code detects motion in a room and sends a notification if movement is detected.

### Materials Required - 
#### Hardware -
1.	Raspberry Pi 4
2.	PIR module
3.	Breadboard
4.	GPIO Extension Board
5.	Resistor 220 ohms
6.	LED Light
7.	LCD
8.	3 Male-to-Male jumper cables
9.	7 Male-to-Female jumper cables

Note - The reference code link is https://github.com/the-raspberry-pi-guy/lcd#Installation

#### Software - 
1.	Raspberry Pi OS installed
2.	Python 3

#### Setup Instructions -
Note: This is assuming you have installed Raspberry Pi and Python already

#### Run the following commands - 

1.  sudo apt install git
2.  cd /home/${USER}/
3.  git clone https://github.com/the-raspberry-pi-guy/lcd.git
4.  cd lcd/
5.  sudo ./install.sh
6.  Reboot the Raspberry Pi
7.  Download the code from https://github.com/ramyapandian1987/Motion_Detector_RPi/blob/main/Motion_Detector.py
8.  Place Motion_Detector.py in the lcd directory

### Connect RPi, PIR Sensor, LED, LCD, and resistor to the breadboard using jumper wires as shown below -

#### PIR sensor pins -

* VCC to pin 2 of RPi

* GND to pin 6 of RPi

* OUT to pin 11 of RPi


#### LCD pins - 

* GND to pin 6 or pin 9 of RPi

* VCC to pin 2 or pin 4 of RPi

* SDA to pin 3 of RPi

* SCL to pin 5 of RPi


#### LED -

* Connect resistor as shown (one end at anypoint and the other end to the ground)

* Connect LED's short leg to the resistor and the long leg to pin 12 of RPi as shown in the picture. 


![image](https://user-images.githubusercontent.com/37421836/166980685-7fe2ce6a-1e3d-4c16-a94b-38b505fcd153.png)

![image](https://user-images.githubusercontent.com/37421836/166981116-0db8aea4-578f-44e5-96aa-3ea2757e4811.png)

To execute – 

The code is available on GitHub at https://github.com/ramyapandian1987/Motion_Detector_RPi/blob/main/Motion_Detector.py
1.	Download the code and execute as shown – 
Python3 Motion_Detector.py
